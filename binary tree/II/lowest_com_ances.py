from binary_tree import TreeNode

def lowestCommonAncestor(root,p,q):
    if root is None or root.val==p.val or root.val==q.val :
        return root
    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)
    if left is None:
        return right
    if right is None:
        return left
    return root

T = TreeNode()
root = T.insert([1,2,3,None,None,5,6,None,None,None,None,7,8])

print(lowestCommonAncestor(root,TreeNode(val=5),TreeNode(val=6)).val)
