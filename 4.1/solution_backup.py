

def solution(banana_list):
    banana_list.sort(reverse=True)
    n = len(banana_list)

    print("banana size:", n)

    g = {}
    for i in range(n):
        g.setdefault(i, [])
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if isLoop(banana_list[i], banana_list[j]):
                print(i, j, " -- ", banana_list[i], banana_list[j])
                g[i].append(j)
                g[j].append(i)

    m = maximum_matching(g, n)

    print("answer:", n - m)
    return n - m

def isLoop(x, y):
    z = x + y
    while y:
        x, y = y, y % x
    z //= x
    return (z & (z - 1)) != 0

def maximum_matching(graph, size):
    m = [i for i in range(size)]
    print(m)

    m = []
    return 1

solution([1, 7, 3, 21, 13, 19])
solution([1, 1])