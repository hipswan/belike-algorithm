from binary_tree import TreeNode

def lowestAncestor(root,p,q):
    if root is None:
        return
    curr = root.val
    if curr < p and curr< q:
        return lowestAncestor(root.right,p,q)
    elif curr>p and curr>q:
        return lowestAncestor(root.left,p,q)
    return root
    

T = TreeNode()
root = T.insert([10,4,13,3,8,11,15,1,6])
print(lowestAncestor(root,3,8))