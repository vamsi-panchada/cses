from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.g = defaultdict(list)
    
    def addEdge(self, u, v):
        self.g[u].append(v)
    
    def khan(self):
        indegree = [0]*self.V
        for _, j in self.g.items():
            for k in j:
                indegree[k-1]+=1
        queue = []
        for i in range(self.V):
            if indegree[i]==0:
                queue.append(i+1)
        cnt = 0
        top_order = []
        while queue:
            u = queue.pop()
            top_order.append(u)
            for i in self.g[u]:
                indegree[i-1]-=1
                if indegree[i-1]==0:
                    queue.append(i)
            cnt += 1
        if cnt!=self.V:
            print("IMPOSSIBLE")
        else:
            print(*top_order)

n, m = map(int, input().split())
g = Graph(n)
for _ in range(m):
    u, v = map(int, input().split())
    g.addEdge(u, v)
g.khan()