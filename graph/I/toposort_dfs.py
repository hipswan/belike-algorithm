# topological sorting using dfs

def toposortdfs(node,adj,vis,st):
    vis[node] = True
    for elem in adj[node]:
        if not vis[elem]:
            toposortdfs(elem,adj,vis,st)
    st.append(node)
graph_ = {0:[],1:[],2:[3],3:[1] ,4:[0,1] ,5:[0,2]}

# graph_ = {1:[2],2:[3],3:[4,6] ,4:[5] ,5:[],6:[5],7:[2,8],8:[9],9:[] }
n = len(graph_)
vis =[0]* (n)
st=[]
topo =[]
for i in range(1,n):
    if not vis[i]:
        toposortdfs(i,graph_,vis,st)
    
    while len(st):  
        topo.append(st.pop())
        
print(topo)
    