from binary_tree import TreeNode
# Left Root Right
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

T = TreeNode()
root = T.insert([1,2,3,4,5])
inorder(root)