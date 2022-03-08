from binary_tree import TreeNode

def balanced_tree(root):
    if root is None:
        return 0
    left = balanced_tree(root.left)
    right = balanced_tree(root.right)
    if left == -1 or right==-1:
        return -1
    if abs(left-right) > 1:
        return -1
    return 1+max(left,right)

T = TreeNode()
root = T.insert([1,2,3,None,None,5,6,None,None,None,None,7,8])

print(balanced_tree(root) != -1)
