def isLoop(x, y):
    z = x + y
    while y:
        x, y = y, y % x
    z //= x
    return (z & (z - 1)) != 0



# Python program to find  
# maximal Bipartite matching. 
  
class GFG: 
    def __init__(self,graph): 
          
        # residual graph 
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 
  
    # A DFS based recursive function 
    # that returns true if a matching  
    # for vertex u is possible 
    def bpm(self, u, matchR, seen): 
  
        # Try every job one by one 
        for v in range(self.jobs): 
  
            # If applicant u is interested  
            # in job v and v is not seen 
            if self.graph[u][v] and seen[v] == False: 
                  
                # Mark v as visited 
                seen[v] = True 
  
                '''If job 'v' is not assigned to 
                   an applicant OR previously assigned  
                   applicant for job v (which is matchR[v])  
                   has an alternate job available.  
                   Since v is marked as visited in the  
                   above line, matchR[v]  in the following 
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],  
                                               matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
  
    # Returns maximum number of matching  
    def maxBPM(self): 
        '''An array to keep track of the  
           applicants assigned to jobs.  
           The value of matchR[i] is the  
           applicant number assigned to job i,  
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs 
          
        # Count of jobs assigned to applicants 
        result = 0 
        for i in range(self.ppl): 
              
            # Mark all jobs as not seen for next applicant. 
            seen = [False] * self.jobs 
              
            # Find if the applicant 'u' can get a job 
            if self.bpm(i, matchR, seen): 
                result += 1
        return result 
  
# 21, 19, 13, 7, 3, 1
# 19,
# 13,
# 7,
# 3,
# 1,

bpGraph =[[0, 0, 0, 0, 0, 1], 
          [0, 0, 0, 1, 1, 1], 
          [0, 0, 0, 0, 1, 1], 
          [0, 1, 0, 0, 1, 0], 
          [0, 1, 1, 1, 0, 0], 
          [1, 1, 1, 0, 0, 0]] 
  
g = GFG(bpGraph) 
  
print ("Maximum number of applicants that can get job is %d " % g.maxBPM()) 
  
# This code is contributed by Neelam Yadav 



l = [1, 3, 7, 13, 19, 21]
l.sort(reverse=True)
n = len(l)

memory = [[0 for i in range(n)]  
                for j in range(n)]

print(memory)

for i in range(n - 1):
    for j in range(i + 1, n):
        if isLoop(l[i], l[j]):
            print("loop", l[i], l[j])
            memory[i][j] = 1
            # memory[j][i] = 1

g = GFG(memory) 
  
print ("Maximum number of applicants that can get job is %d " % g.maxBPM()) 








