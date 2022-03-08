from binary_tree import TreeNode
from collections import deque

def zigZagTraversal(root):
    arr = []
    if root is None:
        return arr
    q = deque()
    q.append(root)
    l2r = True
    while len(q) != 0:
        n= len(q)
        level = [0]* n
        for i in range(n):
            curr = q.popleft()
            idx = i if l2r else n-1-i
            level[idx] = curr.val
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        l2r = not l2r
        arr.append(level)
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5,6,7,8,9])
print(zigZagTraversal(root))