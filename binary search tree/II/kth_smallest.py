from binary_tree import TreeNode   

def kthSmallest(root,k):
    if not root or root.val is None:
        return None
    left = kthSmallest(root.left,k)
    if left:
        return left
    k[0]-=1
    if k[0]==0:
        return root
    return kthSmallest(root.right,k)

T = TreeNode()
root = T.insert([5,3,7,1,4,6,8,None,2])
kthSmallest(root,[3])