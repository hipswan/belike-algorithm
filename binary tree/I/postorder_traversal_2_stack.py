from binary_tree import TreeNode


def postorder(node):
    arr = [] 
    s1 = []
    s2 =[]
    s1.append(node)
    while len(s1) !=0:
        curr = s1.pop()
        s2.append(curr)
        if curr.left is not None:
            s1.append(curr.left)
        if curr.right is not None:
            s1.append(curr.right)
    while len(s2)!=0:
        arr.append(s2.pop().val)
    
    return arr


T = TreeNode()
root = T.insert([1,2,3,4,5])
print(postorder(root))