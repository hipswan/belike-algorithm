from binary_tree import TreeNode

def childSumTree(root):
    if root is None:
        return
    child = 0
    if root.left:
        child+=root.left.val
    if root.right:
        child+=root.right.val
    if child >= root.val:
        root.val=child
    else:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val
    childSumTree(root.left)
    childSumTree(root.right)
    total=0
    if root.left:
        total+=root.left.val
    if root.right:
        total+=root.right.val
    if root.left or root.right:
        root.val = total
    

T = TreeNode()
root = T.insert([1,2,3])

print(childSumTree(root))