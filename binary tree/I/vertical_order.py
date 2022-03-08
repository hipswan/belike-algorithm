from collections import deque
from binary_tree import TreeNode

def verticaltraversal(node):
    arr = []
    if node is None:
        return arr
    q = deque()
    q.append((node,0,0))
    m ={}
    while len(q)!=0:
        curr,line,level = q.popleft()
        if not line in m:
            m[line]={}
        m[line][level] = curr.val
        if curr.left is not None:
            q.append((curr.left,line-1,level+1))
        if curr.right is not None:
            q.append((curr.right,line+1,level+1))
    for _ in m.values():
        col = []
        for __ in _.values():
            col.append(__)
        arr.append(col)
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5])
print(verticaltraversal(root))

