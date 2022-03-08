from binary_tree import TreeNode


def postorder(node):
    arr = [] 
    s = []
    curr = node
    while curr is not None or len(s) !=0:
        if curr is not None:
            s.append(curr)
            curr = curr.left
        else:
            tmp = s[-1].right
            if tmp is None:
                tmp = s.pop()
                arr.append(tmp.val)
                while len(s)!=0 and tmp == s[-1].right:
                    tmp = s.pop()
                    arr.append(tmp.val)
            else:
                curr = tmp
    return arr

T = TreeNode()
root = T.insert([1,2,3,4,5])
print(postorder(root))