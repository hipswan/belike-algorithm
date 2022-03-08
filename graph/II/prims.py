from math import inf
from os import WTERMSIG
from tkinter import N


class Node:
    def __init__(self,v,wt) -> None:
        self.v = v
        self.wt = wt
    
    def __repr__(self) -> str:
        return f' --{self.wt}--> {self.v}'
    
adj=[[Node(1,2),Node(3,6)],[Node(0,2),Node(3,8),Node(4,5),Node(2,3)],[Node(1,3),Node(4,7)],[Node(0,6),Node(1,8)],[Node(1,5),Node(2,7)] ]

n = len(adj)
key = [inf]*n
parent = [-1]*n
mst = [False]*n
key[0] = 0
for i in range(n-1):
    mini = inf
    u =0
    for v in range(n):
        if mst[v] == False and key[v] < mini:
            mini = key[v]
            u=v
    mst[u] =True
    for node in adj[u]:
        if mst[node.v] == False and node.wt < key[node.v]:
            key[node.v] = node.wt 
            parent[node.v] = u

print(parent)