# detect cycle in undirected graph using bfs

from collections import deque

def checkCyclebfs(node,adj,vis):
    q = deque()
    vis[node] = True
    q.append((node,-1))
    while len(q):
        node,prev = q.popleft()
        for elem in adj[node]:
            if not vis[elem]:
                q.append((elem,node))
                vis[elem]=True
            elif prev!=elem:
                return True
    return False


graph_ = {1:[2],2:[1,3,7],3:[2,5] ,4:[6] ,5:[3,7],6:[4],7:[2,5] }
n=len(graph_)
vis=[0]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        if checkCyclebfs(i, graph_,vis):
            print('Undirected Graph Contains Cycle')
