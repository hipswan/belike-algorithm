from binary_tree import TreeNode

def isLeaf(root):
    return root.left is None and root.right is None

def addLeftSide(root,arr):
    curr = root.left
    while curr:
        if not isLeaf(curr):
            arr.append(curr.val)
        if curr.left:
            curr=curr.left
        else:
            curr = curr.right

def addRightSide(root,arr):
    curr = root.right
    tmp = []
    while curr:
        if not isLeaf(curr):
            tmp.append(curr.val)
        if curr.right:
            curr=curr.right
        else:
            curr = curr.left
    n = len(tmp)
    for i in range(n):
        arr.append(tmp[n-1-i])


def addLeaves(root,arr):
    if root is None:
        return
    if isLeaf(root):
        arr.append(root.val)
        return
    addLeaves(root.left,arr)
    addLeaves(root.right,arr)
     

def boundaryTraversal(root):
    arr = []
    if root is None:
        return arr
    
    if not isLeaf(root):
        arr.append(root.val)
    addLeftSide(root,arr)
    addLeaves(root,arr)
    addRightSide(root,arr)
    return arr




T = TreeNode()
root = T.insert([1,2,3,4,5,6,7,8,9])
print(boundaryTraversal(root))