class Node: 
    def __init__(self, x = 0, y = 0, hop = 0): 
        self.x = x
        self.y = y
        self.hop = hop

def solution(src, dest):
    current = Node(src % 8, src / 8)
    target = Node(dest % 8, dest / 8)
    return move(current, target)

def move(src, dst):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    memory = [[-1 for i in range(8)]  
                    for j in range(8)]

    queue = []
    queue.append(src)

    while(len(queue) > 0):
        node = queue[0]
        queue.pop(0)

        if (node.x == dst.x and node.y == dst.y):
            return node.hop

        for i in range(8):

            x = node.x + dx[i]
            y = node.y + dy[i]

            inside = isInside(x,y)
            if (inside):
                visited = memory[y][x] != -1
                if (not visited):
                    memory[y][x] = 1
                    queue.append(Node(x, y, node.hop + 1))

    return -1
    

def isInside(x, y):
    if (x >= 0 and x <= 7 and y >= 0 and y <= 7):
        return True
    return False

print(solution(0, 1)) # 3 (0,0) (0, 1)
print(solution(19, 36)) # 1 (2,3) (4,4)

# print(isInside(0,0))
# print(isInside(8,8))
# print(isInside(9,1))
# print(isInside(1,9))
# print(isInside(-1,0))
# print(isInside(0,-1))