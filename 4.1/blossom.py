class Node:
    index = 0

    def __init__(self):
        self.neighbors = []
        self.is_visited = False
        self.parent = None
        self.mate = None
        self.index = Node.index
        Node.index += 1


    def __repr__(self):
        return str(self.index)


class SuperNode(Node):
    
    def __init__(self):
        Node.__init__(self)
        self.subnodes = []
        self.original_edges = []


    def circle(self, node):
        for i, v in enumerate(self.subnodes):
            if v == node:
                break
        assert i < len(self.subnodes)

        if i > 0 and self.subnodes[i].mate == self.subnodes[i-1] or i == 0 and self.subnodes[i].mate == self.subnodes[-1]:
            return self.subnodes[i::-1] + self.subnodes[:i:-1]
        else:
            return self.subnodes[i::] + self.subnodes[:i]


class Path:

    def __init__(self):
        self.nodes = []


    def head(self):
        return self.nodes[0]


    def tail(self):
        return self.nodes[-1]


    def replace_head(self):
        assert isinstance(self.nodes[0], SuperNode)
        snode = self.nodes.pop(0)
        for node in snode.subnodes:
            if self.nodes[0] in node.neighbors:
                if node.mate == None:
                    self.nodes.insert(0, node)
                else:
                    for v in snode.circle(node):
                        self.nodes.insert(0, v)
                return


    def replace_tail(self):
        assert isinstance(self.nodes[-1], SuperNode)
        snode = self.nodes.pop()
        for node in snode.subnodes:
            if self.nodes[-1] in node.neighbors:
                if node.mate == None:
                    self.nodes.append(node)
                else:
                    for v in snode.circle(node):
                        self.nodes.append(v)
                return


    def __repr__(self):
        return str(self.nodes)


class Match:

    def __init__(self, nodes):
        self.nodes = nodes
        self.freenodes = []
        for node in nodes:
            self.freenodes.append(node)
        self.supernodes = []


    def from_edges(N, edges):
        nodes = [Node() for i in range(N)]
        for i, j in edges:
            nodes[i].neighbors.append(nodes[j])
        return Match(nodes)


    def clear_nodes(self):
        for node in self.nodes:
            node.is_visited = False
            node.parent = None


    def find_augmenting_path(self, root):
        self.clear_nodes()
        queue = [root]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            cur_node.is_visited = True
            for node in cur_node.neighbors:
                if node == cur_node.parent:
                    continue

                elif node.is_visited:
                    cycle = self.find_cycles(node, cur_node)
                    if len(cycle) % 2 == 1:
                        snode = self.shrink_blossom(cycle)
                        self.supernodes.append(snode)
                        for v in cycle:
                            if v in queue:
                                queue.remove(v)
                            if v.is_visited:
                                snode.is_visited = True
                                snode.parent = v.parent
                        queue.append(snode)
                        break

                elif node.mate == None:
                    node.parent = cur_node
                    return self.construct_augmenting_path(node)

                else:
                    node.is_visited = True
                    node.mate.is_visited = True
                    node.parent = cur_node
                    node.mate.parent = node
                    queue.append(node.mate)
        # raise Exception('cannot find an augmenting path')


    def unmatched_nodes(self):
        self.maximum_matching()

        count = 0
        for node in self.nodes:
            if node.mate != None:
                count += 1

        # if len(self.nodes) % 2 != 0:
        #     count -= 1
        return len(self.nodes) - count


    def maximum_matching(self):
        while len(self.freenodes) > 0:
            for node in self.freenodes:
                # print("try")
                # try:
                path = self.find_augmenting_path(node)

                # self.invert_path(path)
                # print(path)
                if path and len(path.nodes) % 2 == 0:
                    for i in range(0, len(path.nodes), 2):
                        path.nodes[i].mate = path.nodes[i+1]
                        path.nodes[i+1].mate = path.nodes[i]
                else:
                    continue

                self.freenodes.remove(path.nodes[0])
                self.freenodes.remove(path.nodes[-1])
                break
                # except Exception as e:
                #     continue
                    # print("error")
            else:
                break


    def invert_path(self, path):
        # print("inverted")
        assert len(path.nodes) % 2 == 0
        # print("pass inverted")
        for i in range(0, len(path.nodes), 2):
            path.nodes[i].mate = path.nodes[i+1]
            path.nodes[i+1].mate = path.nodes[i]


    def construct_augmenting_path(self, node):
        path = Path()
        path.nodes.append(node)
        node = node.parent
        path.nodes.append(node)
        while node.mate != None:
            node = node.parent
            path.nodes.append(node)

        while len(self.supernodes) > 0:
            snode = self.supernodes.pop()
            self.expand_supernode(snode)
            if snode == path.head():
                path.replace_head()
            elif snode == path.tail():
                path.replace_tail()

        while path.nodes[0].mate != None:
            path.nodes.insert(path.nodes[0].parent, 0)
            
        while path.nodes[-1].mate != None:
            path.nodes.append(path.nodes[-1].parent)

        return path


    def find_cycles(self, node1, node2):
        def find_ancestors(node):
            ancestors = [node]
            while node.parent != None:
                node = node.parent
                ancestors.append(node)
            return ancestors

        ancestors1 = find_ancestors(node1)
        ancestors2 = find_ancestors(node2)
        i = len(ancestors1) - 1
        j = len(ancestors2) - 1
        while ancestors1[i] == ancestors2[j]:
            i -= 1
            j -= 1

        cycle = ancestors1[:i+1] + ancestors2[j+1::-1]
        return cycle


    def shrink_blossom(self, blossom):
        snode = SuperNode()
        for node in blossom:
            snode.subnodes.append(node)
            for adj_node in node.neighbors:
                if adj_node not in blossom:
                    snode.original_edges.append((node, adj_node))

        for node1, node2 in snode.original_edges:
            node1.neighbors.remove(node2)
            node2.neighbors.remove(node1)
            node2.neighbors.append(snode)
            snode.neighbors.append(node2)

        return snode


    def expand_supernode(self, snode):
        assert isinstance(snode, SuperNode)
        for node1, node2 in snode.original_edges:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
            node2.neighbors.remove(snode)
            snode.neighbors.remove(node2)

from fractions import gcd

def loop(x, y):
    if x == y:
        return False
    if x < y:
        x, y = y, x

    if (x+y) % 2 == 1:
        return 1

    n = gcd(x,y)
    x, y = x/n, y/n
    x, y = x - y, y * 2

    return loop(x, y)

def solution(banana_list):
    banana_list.sort(reverse=True)
    n = len(banana_list)

    nodes = [Node() for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            # m, n = max(banana_list[i], banana_list[j]), min(banana_list[i], banana_list[j])
            # print(m, n)
            if loop(banana_list[i], banana_list[j]):
                # print(i,j, banana_list[i], banana_list[j])
                nodes[i].neighbors.append(nodes[j])
                nodes[j].neighbors.append(nodes[i])
    
    # print("xxxxxxx")
    # for i in range(n):
    #     print(i, banana_list[i], nodes[i].neighbors)

    #     for j in range(len(nodes[i].neighbors)):
    #         print("-", banana_list[nodes[i].neighbors[j].index])
    #         # print("-", banana_list[])

    
    
    match = Match(nodes)
    unmatched_nodes = match.unmatched_nodes()

    print(unmatched_nodes)
    return unmatched_nodes

x = None
# print(not x and x.nodes)
if x:
    if x.nodes % 2 == 0:
        print("hello")

solution([1, 7, 3, 21, 13, 19])
solution([1, 1])
solution([24, 22, 21, 23])
solution([24, 22, 21])
solution([1, 7, 3, 21, 13, 19, 1, 7, 3, 21, 13, 19, 1, 1, 7, 3, 21, 13, 19, 1, 7, 3, 21, 13, 19, 1, 123])
solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
solution([1073741723,1073741724,1073741725,1073741726,1073741727,1073741728,1073741729,1073741730,1073741731,1073741732,1073741733,1073741734,1073741735,1073741736,1073741737,1073741738,1073741739,1073741740,1073741741,1073741742,1073741743,1073741744,1073741745,1073741746,1073741747,1073741748,1073741749,1073741750,1073741751,1073741752,1073741753,1073741754,1073741755,1073741756,1073741757,1073741758,1073741759,1073741760,1073741761,1073741762,1073741763,1073741764,1073741765,1073741766,1073741767,1073741768,1073741769,1073741770,1073741771,1073741772,1073741773,1073741774,1073741775,1073741776,1073741777,1073741778,1073741779,1073741780,1073741781,1073741782,1073741783,1073741784,1073741785,1073741786,1073741787,1073741788,1073741789,1073741790,1073741791,1073741792,1073741793,1073741794,1073741795,1073741796,1073741797,1073741798,1073741799,1073741800,1073741801,1073741802,1073741803,1073741804,1073741805,1073741806,1073741807,1073741808,1073741809,1073741810,1073741811,1073741812,1073741813,1073741814,1073741815,1073741816,1073741817,1073741818,1073741819,1073741820,1073741821,1073741822])