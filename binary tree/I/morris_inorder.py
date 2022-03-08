from binary_tree import TreeNode


def morrisinorder(node):
    arr =[]
    curr = node
    while curr is not None:
        if curr.left is None:
            arr.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right != curr:
                prev = prev.right
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                arr.append(curr.val)
                curr = curr.right
    
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5])
print(morrisinorder(root))