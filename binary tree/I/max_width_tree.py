from collections import deque
from binary_tree import TreeNode
def maxWidthBinaryTree(node):
    ans = 0
    if not node:
        return ans
    q =deque()
    q.append((node,0))
    ans = 1
    while len(q) !=0:
        n = len(q)
        _,min = q[0]
        last,first=0,0
        for i in range(n):
            curr,curr_id = q.popleft()
            curr_id = curr_id-min
            if i==0:
                first = curr_id
            if i == n-1:
                last = curr_id
            if curr.left is not None:
                q.append((curr.left,2*curr_id+1))
            if curr.right is not None:
                q.append((curr.right,2*curr_id+2))
            
            
        ans=max(ans,last-first+1)
    
    return ans

T = TreeNode()
root = T.insert([1,2,3,4,None,None,5])
print(maxWidthBinaryTree(root))


    