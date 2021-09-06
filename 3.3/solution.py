# visit = set()

# x1 = Node(0, 0)
# x2 = Node(0, 0, False)

# visit.add(x1)
# visit.add(x2)

# print(Node(0, 0, True) in visit)
# print(Node(0, 0) in visit)

# print(x1 in visit)
# print(x2 in visit)

class Node: 
    def __init__(self, x = 0, y = 0, hop = 0, wall_removed = False):
        self.x = x
        self.y = y
        self.hop = hop
        self.wall_removed = wall_removed

def solution(map):
    x = len(map[0]) - 1
    y = len(map) - 1

    start = Node(0, 0)
    target = Node(x, y)

    # print(start.x, start.y)
    # print(target.x, target.y)

    hop = move(map, start, target)
    print(hop)
    return hop

def move(map, src, dst):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = set()

    queue = []
    queue.append(src)

    while(len(queue) > 0):
        node = queue[0]
        queue.pop(0)

        # print(node.x, node.y, '--', node.hop)
        if (node.x == dst.x and node.y == dst.y):
            return node.hop + 1
        
        if (node.x, node.y, node.wall_removed) in visited:
            continue
        
        visited.add((node.x, node.y, node.wall_removed))

        for i in range(4):

            x = node.x + dx[i]
            y = node.y + dy[i]

            inside = x >= 0 and x <= dst.x and y >= 0 and y <= dst.y
            if inside:
                haveWall = map[y][x] == 1
                if haveWall and not node.wall_removed:
                    n = Node(x, y, node.hop+1, True)
                    queue.append(n)
                elif not haveWall:
                    n = Node(x, y, node.hop+1, node.wall_removed)
                    queue.append(n)

    return 0

# def move(map, src, dst):

#     memory = [[0 for i in range(dst.x+1)] for j in range(dst.y+1)]
#     memory[0][0] = 1

#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]

#     queue = []
#     queue.append(src)

#     print(memory)

#     while(len(queue) > 0):
#         node = queue[0]
#         queue.pop(0)

#         # print(node.x, node.y, '--', node.hop)
#         if (node.x == dst.x and node.y == dst.y):
#             return node.hop + 1
        
#         for i in range(4):

#             x = node.x + dx[i]
#             y = node.y + dy[i]
#             # print("append", x, y, i, j)

#             inside = insideMap(dst, x, y)
#             if inside:

#                 print(y+1, x+1)
#                 visited = memory[y][x] != 0
#                 if not visited:

#                     memory[y][x] = 1
#                     # print("walk", y, x, '--', node.hop+1)

#                     haveWall = map[y][x] == 1
#                     if haveWall and not node.wall_removed:
#                         n = Node(x, y, node.hop+1, True)
#                         queue.append(n)
#                     elif not haveWall:
#                         n = Node(x, y, node.hop+1, node.wall_removed)
#                         queue.append(n)

#     return 0


def insideMap(dst, x, y):
    if x >= 0 and x <= dst.x and y >= 0 and y <= dst.y:
        return True
    return False


solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
solution([[0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 0, 0],
[1, 1, 0, 1, 1, 0, 1],
[0, 1, 0, 0, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 0, 0]])

# solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])