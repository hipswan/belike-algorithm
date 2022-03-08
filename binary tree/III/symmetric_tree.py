from binary_tree import TreeNode

def symmetricTree(root):
    if root is None:
        return False
    return symmetryCheck(root.left ,root.right)

def symmetryCheck(left,right):
    if left is None or right is None:
        return left == right
    return left.val == right.val and symmetryCheck(left.right, right.left) and symmetryCheck(left.left, right.right)


T = TreeNode()
root = T.insert([1,2,2])

print(symmetricTree(root))