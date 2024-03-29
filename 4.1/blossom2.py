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
        raise Exception('cannot find an augmenting path')


    def unmatched_nodes(self):
        self.maximum_matching()

        count = 0
        for node in self.nodes:
            if node.mate != None:
                count += 1

        if count % 2 != 0:
            count -= 1
        return len(self.nodes) - count


    def maximum_matching(self):
        while len(self.freenodes) > 0:
            for node in self.freenodes:
                try:
                    path = self.find_augmenting_path(node)

                    self.invert_path(path)
                    self.freenodes.remove(path.nodes[0])
                    self.freenodes.remove(path.nodes[-1])
                    break
                except Exception as e:
                    continue
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

def blossom(banana_list):
    banana_list.sort(reverse=True)
    n = len(banana_list)

    nodes = [Node() for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if loop(banana_list[i], banana_list[j]):
                nodes[i].neighbors.append(nodes[j])
                nodes[j].neighbors.append(nodes[i])

    
    
    match = Match(nodes)
    unmatched_nodes = match.unmatched_nodes()

    return unmatched_nodes