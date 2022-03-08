from binary_tree import TreeNode
# Root Left Right 
def preorder(node):
    if node is None:
        return 
    print(node.val)
    preorder(node.left)
    preorder(node.right)

T = TreeNode()
root = T.insert([])
preorder(root)