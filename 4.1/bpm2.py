class Graph: 
    def __init__(self,graph): 
        self.graph = graph
        self.size = len(graph)
  
    def bpm(self, u, matchR, seen): 
        for v in range(self.size): 
            if self.graph[u][v] and seen[v] == False: 
                seen[v] = True 
  
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
  
    def maximum_matching(self): 
        matchR = [-1] * self.size 
          
        result = 0 
        for i in range(self.size): 
            seen = [False] * self.size 
              
            if self.bpm(i, matchR, seen): 
                result += 1
        return self.size - result 

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

    # def isLoop(x, y):
    #     z = x + y
    #     while y:
    #         x, y = y, y % x
    #     z //= x
    #     return (z & (z - 1)) != 0

    # def gcd(x, y):
    #     while(y):
    #         x, y = y, x % y
    #     return x
    def is_forever(x, y):
        if y > x:
            x, y = y, x  # Swap them for an integer division.
        z, r = divmod(x, y)
        if r:
            return True  # Indivisible
        # (z - 1) & z is False for a power of two, but c should be False
        # for a power of two - 1, so add one on both sides.
        return bool(z & (z + 1))
        
    def is_power_of_two(x):
        """ Quick hack to check if x==2^n
        """
        return (x & (x - 1)) == 0 and x != 0  # The second condition is useless here (nb of bananas never 0)


    def has_exit(i, j):
        """ Check if the sequence starting with the given numbers
        will reach an exit point.
        """
        return is_power_of_two((i+j) / gcd(i,j))


    # def loop(x, y):
    #     if x == y:
    #         return False
    #     if x < y:
    #         x, y = y, x

    #     if (x+y) % 2 == 1:
    #         return 1

    #     n = gcd(x,y)
    #     x, y = x/n, y/n
    #     x, y = x - y, y * 2

    #     return loop(x, y)
    # def loop(a, b):
    #     compute = {}

    #     def cal(x, y):
    #         if x == y:
    #             return False
    #         if x < y:
    #             x, y = y, x
    #         # print("compute", compute)
    #         # print(x, y)
    #         # compute.add((x, y))


    #         x, y = x - y, y * 2

    #         if (x, y) in compute:
    #             # print("return", compute.get((x,y)))
    #             return True
    #         # compute[(x,y)] = True
    #         # print(x, y)
    #         # print("end")
    #         if x == y:
    #             compute[(x,y)] = False
    #             return False
    #         else:
    #             # print(x,y,"added")
    #             compute[(x,y)] = True
    #             return cal(x, y)
    #     return cal(a, b)

    # def loop(a, b):
    #     compute = {}

    #     def cal(x, y):
    #         if x > y:
    #             x, y = y, x
    #         # print("compute", compute)
    #         # print(x, y)
    #         # compute.add((x, y))

    #         if (x, y) in compute:
    #             return compute[(x, y)]

    #         x, y = x - y, y * 2
    #         # print(x, y)
    #         # print("end")
    #         if x == y:
    #             compute[(x,y)] = False
    #             return False
    #         else:
    #             compute[(x,y)] = True
    #             cal(x, y)
    #     return cal(a, b)
        

    graph = list([0] * n for i in range(n))
    for i in range(n-1):
        for j in range(i+1, n):
            # print(banana_list[i], banana_list[j], is_forever(banana_list[i], banana_list[j]))
            if loop(banana_list[i], banana_list[j]):
                graph[i][j] = 1
                graph[j][i] = 1

    # print("--", banana_list)
    # for i in range(len(graph)):
    #     print(banana_list[i], graph[i])

    # print(loop(19, 13))
    
    # graph = [[0, 1, 1, 0, 0, 1],
    #         [1, 0, 0, 1, 1, 1],
    #         [1, 0, 0, 1, 0, 1],
    #         [0, 1, 1, 0, 1, 0],
    #         [0, 1, 0, 1, 0, 0],
    #         [1, 1, 1, 0, 0, 0]]

    # graph = [[0, 0], [0, 0]]

    # print(graph)

    m = Graph(graph).maximum_matching()
    return m

print("xxxxxxxxxxxxxxxx")
print(solution([1, 1]))
print("xxxxxxxxxxxxxxxx")
print(solution([1, 3, 7, 13, 19, 21]))
print("xxxxxxxxxxxxxxxx")
print(solution([1073741723,1073741724,1073741725,1073741726,1073741727,1073741728,1073741729,1073741730,1073741731,1073741732,1073741733,1073741734,1073741735,1073741736,1073741737,1073741738,1073741739,1073741740,1073741741,1073741742,1073741743,1073741744,1073741745,1073741746,1073741747,1073741748,1073741749,1073741750,1073741751,1073741752,1073741753,1073741754,1073741755,1073741756,1073741757,1073741758,1073741759,1073741760,1073741761,1073741762,1073741763,1073741764,1073741765,1073741766,1073741767,1073741768,1073741769,1073741770,1073741771,1073741772,1073741773,1073741774,1073741775,1073741776,1073741777,1073741778,1073741779,1073741780,1073741781,1073741782,1073741783,1073741784,1073741785,1073741786,1073741787,1073741788,1073741789,1073741790,1073741791,1073741792,1073741793,1073741794,1073741795,1073741796,1073741797,1073741798,1073741799,1073741800,1073741801,1073741802,1073741803,1073741804,1073741805,1073741806,1073741807,1073741808,1073741809,1073741810,1073741811,1073741812,1073741813,1073741814,1073741815,1073741816,1073741817,1073741818,1073741819,1073741820,1073741821,1073741822]))

# GFG(bpGraph)