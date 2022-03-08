from collections import deque
from binary_tree import TreeNode

def bottomview(node):
    arr = []
    if node is None:
        return arr
    q = deque()
    q.append((node,0))
    m ={}
    while len(q)!=0:
        curr,line = q.popleft()
        m[line] = curr.val
        if curr.left is not None:
            q.append((curr.left,line-1))
        if curr.right is not None:
            q.append((curr.right,line+1))
    arr= [ x for _,x in sorted(m.items() , key=lambda x:x[0])]
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5])
print(bottomview(root))

