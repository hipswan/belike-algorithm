# kosa raju algorithm

import display_svg as d


adj = {1:[2],2:[3,4],3:[1],4:[5],5:[]}
n = len(adj)
vis = [0] * (n+1)
st = [] 
def dfs(node, adj,st,vis):
    vis[node] = -1
    for elem in adj[node]:
        if not vis[elem]:
            dfs(elem,adj,st,vis)
    st.append(node)

def revdfs(node,adj,vis,arr):
    vis[node] =-1  
    arr.append(node)
    for elem in adj[node]:
        if not vis[elem]:
            revdfs(elem,adj,vis,arr)
    


for i in range(1,n+1):
    if not vis[i]:
        dfs(i,adj,st,vis)

print(st)
transpose = {}
for key,value in adj.items():
    
    for node in value:
        transpose[node] = transpose.get(node,[]) + [key]
       

print(transpose)
scc= []
vis = [0]*(n+1)
while len(st):
    node = st.pop()
    arr =[]
    if not vis[node]:
        revdfs(node,transpose,vis,arr)
        scc.append(arr)

print(scc)



