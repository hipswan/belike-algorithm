from binary_tree import TreeNode
# Left Right Root
def postorder(node):
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.val)

T = TreeNode()
root = T.insert([1,2,3,4,5])
postorder(root)