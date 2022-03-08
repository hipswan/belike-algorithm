from binary_tree import TreeNode   

def kthLargest(root,k):
    if not root or root.val is None:
        return None
    right = kthLargest(root.right,k)
    if right:
        return right
    k[0]-=1
    if k[0]==0:
        return root
    return kthLargest(root.left,k)

T = TreeNode()
root = T.insert([5,3,7,1,4,6,8,None,2])
kthLargest(root,[3])