from binary_tree import TreeNode

def maxdepth(root):
    if root is None:
        return 0
    left = maxdepth(root.left)
    right = maxdepth(root.right)
    return 1+max(left,right)

T = TreeNode()
root = T.insert([1,2,3,4,5,6,7,8,9])
print(maxdepth(root))