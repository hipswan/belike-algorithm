from queue import PriorityQueue
from math import inf
q = PriorityQueue()

class Node:
    def __init__(self,v,wt) -> None:
        self.v = v
        self.wt = wt
    
    def __repr__(self) -> str:
        return f' --{self.wt}--> {self.v}'
    
adj=[[Node(1,2),Node(3,6)],[Node(0,2),Node(3,8),Node(4,5),Node(2,3)],[Node(1,3),Node(4,7)],[Node(0,6),Node(1,8)],[Node(1,5),Node(2,7)] ]

n = len(adj)

dist = [inf] * n
src = 0
dist[src] = 0
q.put((0,0))
while not q.empty():
    _,node = q.get()
    for elem in adj[node]:
        if dist[node] + elem.wt < dist[elem.v]:
            dist[elem.v] = dist[node] + elem.wt
            q.put((dist[elem.v],elem.v))
print(dist)
