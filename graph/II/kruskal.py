
from functools import cmp_to_key

class DisjointSet:
    def __init__(self,nodes) -> None:
        self.parent =[i for i in range(nodes+1)]
        self.rank =[0 for i in range(nodes+1)]
    
    def findPar(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2):

        node1 = self.parent[node1]
        node2 = self.parent[node2]
        if self.rank[node1] > self.rank[node2]:
            self.parent[node2] = node1
        elif self.rank[node2] > self.rank[node1]:
            self.parent[node1] = node2
        else:
            self.parent[node2] = node1
            self.rank[node1]+=1
    
class Node:
    def __init__(self,u,v,wt) -> None:
        self.u = u
        self.v = v
        self.wt = wt
    
    def __repr__(self) -> str:
        return f'{self.u} --{self.wt}--> {self.v}'
    
def compare(node1,node2):
    return node1.wt - node2.wt
    
# initialize graph
graph = [Node(1,2,2),Node(1,4,1),Node(1,5,4),Node(5,4,9),Node(4,3,5),Node(3,6,8),Node(2,6,7),Node(2,3,3),Node(4,2,3)]

# create disjoint set with length of nodes in graph
dis_set = DisjointSet(len(graph))

# sort graph according to weight
graph_sorted = sorted(graph,key=cmp_to_key(compare))

cost_mst = 0
mst = []
for node in graph_sorted:
    if dis_set.findPar(node.u) != dis_set.findPar(node.v):
        cost_mst+=node.wt
        mst.append(node)
        dis_set.union(node.u,node.v)

print(cost_mst,mst)

# TC -- > O(nlog(n))
# SC -- > O(n)



        
