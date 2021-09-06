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
        if result % 2 != 0:
            result -= 1
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

    graph = list([0] * n for i in range(n))
    for i in range(n-1):
        for j in range(i+1, n):
            if loop(banana_list[i], banana_list[j]):
                graph[i][j] = 1
                graph[j][i] = 1

    m = Graph(graph).maximum_matching()
    return m