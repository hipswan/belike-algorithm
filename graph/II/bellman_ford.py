# single source shortest path

from functools import cmp_to_key
from math import inf
from tkinter import N


class Node:
    def __init__(self,u,v,wt) -> None:
        self.u = u
        self.v = v
        self.wt = wt
    
    def __repr__(self) -> str:
        return f'{self.u} --{self.wt}--> {self.v}'

# initialize graph
graph = [Node(1,2,2),Node(1,4,1),Node(1,5,4),Node(5,4,9),Node(4,3,5),Node(3,6,8),Node(2,6,7),Node(2,3,3),Node(4,2,3)]



n = len(graph)
dist =[inf]* (n+1)
dist[1] = 0
for i in range(n):
    for node in graph:
        if dist[node.u] + node.wt < dist[node.v]:
            dist[node.v] = dist[node.u] + node.wt

# detect negative cycle
flag = 0
for node in graph:
    if dist[node.u] + node.wt < dist[node.v]:
        flag =1
        print('neg cycle detected')

print(dist)

