

from math import inf

# All pair shortest path
adj_matrix =[[0,3,-1,5],[2,0,inf,8],[inf,1,0,inf],[inf,inf,2,0]]
n = len(adj_matrix)

dist = list(adj_matrix)
for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if j == k:
                continue
            if dist[i][k] == inf or dist[k][j] == inf:
                continue
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# detect neg cycle
for i in range(n):
    for j in range(n):
        if dist[i][j] < 0:
            print('neg cycle detected')
            break
    if j!=n-1 or dist[i][j] <0:
        break  

# tc --> o(n^3)
# sc --> o(n^2)
