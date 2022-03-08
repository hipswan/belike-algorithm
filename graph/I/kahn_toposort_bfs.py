# Kahn algo: topological sort
# linear ordering of vertices such that if there is an edge u --> v , u appears before v
from collections import deque

graph_ = {0:[],1:[],2:[3],3:[1] ,4:[0,1] ,5:[0,2]}
n=len(graph_)
topo=[0]*n
in_deg = [0]*(n)
for i in range(n):
    for elem in graph_[i]:
        in_deg[elem]+=1
q = deque()
for i in range(n):
    if in_deg[i] == 0:
        q.append(i)

idx = 0
while len(q):
    node = q.popleft()
    topo[idx] = node
    idx+=1
    for elem in graph_[node]:
        in_deg[elem]-=1
        if in_deg[elem] == 0:
            q.append(elem)

print(topo)


