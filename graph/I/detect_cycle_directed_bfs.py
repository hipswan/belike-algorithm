# detect cycle in directed graph using bfs

# Kahn algo: topological sort
# linear ordering of vertices such that if there is an edge u --> v , u appears before v
from collections import deque


graph_ = {1:[2],2:[3],3:[4,6] ,4:[5] ,5:[],6:[5],7:[2,8],8:[9],9:[] }

n=len(graph_)
topo=[0]*(n+1)
in_deg = [0]*(n+1)
for i in range(1,n+1):
    for elem in graph_[i]:
        in_deg[elem]+=1
q = deque()
for i in range(1,n+1):
    if in_deg[i] == 0:
        q.append(i)

idx = 1
while len(q):
    node = q.popleft()
    topo[idx] = node
    idx+=1
    for elem in graph_[node]:
        in_deg[elem]-=1
        if in_deg[elem] == 0:
            q.append(elem)
print(topo)
if (idx-1) != n:
    print('Directed Graph contains Cycle')


