from binary_tree import TreeNode


def preorder(node):
    arr = []
    s =[]
    if node is None:
        return arr
    s.append(node)
    while len(s)!=0:
        curr = s.pop()
        arr.append(curr.val)
        if curr.right is not None:
            s.append(curr.right)
        if curr.left is not None:
            s.append(curr.left)
    return arr


T = TreeNode()
root = T.insert([1,2,3,4,5])
print(preorder(root))
