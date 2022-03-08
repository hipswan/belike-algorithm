# detect cycle in directed graph dfs




def checkCycleDirectedDfs(node,adj,vis,dfsvis):
    vis[node] = True
    dfsvis[node] =True
    for elem in adj[node]:
        if not vis[elem]:
            if checkCycleDirectedDfs(elem,adj,vis,dfsvis):
                return True
        elif dfsvis[elem]:
            return True
    dfsvis[node] = False
    return False


graph_ = {1:[2],2:[3,7],3:[4,6] ,4:[5] ,5:[],6:[5],7:[8],8:[9],9:[7] }
n=len(graph_)
vis=[0]*(n+1)
# to check whether nodes are visted in same dfs calls 
dfsvis = [0]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        if checkCycleDirectedDfs(i,graph_,vis,dfsvis):
            print('Directed Graph Contain Cycle')

# tc --> o(n)
# sc --> o(n)