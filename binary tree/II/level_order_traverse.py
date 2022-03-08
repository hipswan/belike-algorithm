from binary_tree import TreeNode
from collections import deque

def levelordertraversal(root):
    arr =[]
    if not root:
        return arr
    q = deque()
    q.append(root)
    while len(q)!=0:
        n = len(q)
        level =[] 
        for i in range(n):

            curr = q.popleft()
            level.append(curr.val)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        arr.append(level)
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5,6,7,8,9])
print(levelordertraversal(root))