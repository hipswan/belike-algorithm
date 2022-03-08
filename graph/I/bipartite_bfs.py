# bipartite graph are thoe graphs that can be colored just using 2 colors
# if graph doesn't contain cycle then it is bipartite
# If graph contains cycle of even length then it is bipatite
# If graph contians cycle of odd length then it is [not] bipartite

from collections import deque


def checkBipartite(node,adj,color):
    q = deque()
    q.append(node)
    color[node] = 0
    while len(q):
        node = q.popleft()
        for elem in adj[node]:
            if color[elem] ==-1:
                q.append(elem)
                color[elem] = 1 - color[node]
            elif color[elem] == color[node]:
                return False
    return True

# Not Bipartite
graph_ = {1:[2],2:[1,3,9],3:[4] ,4:[3,5] ,5:[4,6,8],6:[5,7],7:[2,6,9],8:[5],9:[2,7] }

# graph_ = {1:[2],2:[1,3,7],3:[4] ,4:[3,5] ,5:[4,6,8],6:[5,7],7:[2,6],8:[5] }
n=len(graph_)
color = [-1]*(n+1)
for i in range(1,n+1):
    if color[i] == -1:
        if checkBipartite(i,graph_,color): 
            print('It is a Bipartite Graph')