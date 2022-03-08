from binary_tree import TreeNode

def flattenTreeRec(root):
    if root is None:
        return
    flattenTreeRec(root.right)
    flattenTreeRec(root.left)
    root.right = prev
    root.left = None
    prev= root
    return root

def flattenTreeMorris(root):
    curr = root
    while curr:
        if curr.left:
            tmp = curr.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right 

def flattenTreeIterative(root):
    s = []
    if not root:
        return
    s.append(root)
    while len(s) != 0 :
        curr = s.pop()
        if curr.right:
            s.append(curr.right)
        if curr.left:
            s.append(curr.left)
        if len(s)!=0:
            curr.right = s[-1]
        curr.left = None
    return root
prev = None
T = TreeNode()
root = T.insert([1,2,3])

print(flattenTreeIterative(root))