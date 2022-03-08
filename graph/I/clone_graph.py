# clone a graph using dfs



class Node:
    def __init__(self,val=0,neighbors=[]) -> None:
        self.val = val
        self.neighbors =neighbors
    
    def __repr__(self) -> str:
        return f'{self.val} -- > {self.neighbors}'

dict_ = {}
def clone(node):
    if node.val in dict_:
        return dict_[node.val]
    copy = Node(val = node.val)
    dict_[node.val] = copy
    for neighbor in node.neighbors:
        copy.neighbors.append(clone(neighbor))
    return copy

graph = Node(val=1,neighbors=[Node(val=2)])

if graph:
    clone(graph)

