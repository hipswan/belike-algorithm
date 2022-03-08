from queue import Queue

class node:
    def __init__(self, color):
        self.color = color
        self.neighbors = set()

def canPaint(nodes,v,m):
    maxColor =1

    visited = [0 for i in range(v)]
    for i in range(v):
        if visited[i] == 1:
            continue
        visited[i] = 1
        q = Queue()
        q.put(i)
        while not q.empty():
            u =q.get()

            for j in nodes[u].neighbors:
                
                if nodes[j].color == nodes[u].color:

                    nodes[j].color+=1
                
                maxColor = max(maxColor,nodes[j].color,nodes[u].color)

                if maxColor > m:
                    print(maxColor)
                    return False

                if visited[j] == 0:
                    visited[j] = 1
                    q.put(j)
    return True



graph = [ [ 0, 1, 1, 1 ],
          [ 1, 0, 1, 0 ],
          [ 0, 1, 0, 1 ],
          [ 1, 0, 1, 0 ] ]
v = 4
m = 3
nodes = []
for i in range(v):
    nodes.append(node(1))

for i in range(v):
    for j in range(v):
        if graph[i][j] == 1:
            nodes[i].neighbors.add(j)
    
print(canPaint(nodes,v, m))