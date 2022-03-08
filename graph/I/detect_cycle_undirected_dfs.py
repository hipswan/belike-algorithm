# detect cycle in undirected graph using dfs



from sqlalchemy import true


def checkCycledfs(node,prev,adj,vis):
    vis[node] = True
    for elem in adj[node]:
        if not vis[elem]:
            vis[elem] =True
            if checkCycledfs(elem,node,adj,vis):
                return True
        elif elem!=prev:
            return True
    return False

graph_ = {1:[2],2:[1,3,7],3:[2,5] ,4:[6] ,5:[3,7],6:[4],7:[2,5] }
n=len(graph_)
vis=[0]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        if checkCycledfs(i,-1, graph_,vis):
            print('Undirected Graph Contains Cycle')