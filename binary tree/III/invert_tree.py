from binary_tree import TreeNode

def invertTree(root):
    if not root:
        return
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.right =left
    root.left = right
    return root
T = TreeNode()
root = T.insert([1,2,3])

print(invertTree(root))