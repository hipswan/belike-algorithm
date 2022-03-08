from binary_tree import TreeNode


def inorder(node):
    arr = []
    curr  = node
    s =[]
    while True:
        if curr is not None:
            s.append(curr)
            curr=curr.left
        else:
            if len(s) == 0:
                break
            else:
                curr = s.pop()
                arr.append(curr.val)
                curr=curr.right
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5])
print(inorder(root))

