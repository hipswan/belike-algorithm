from binary_tree import TreeNode


def rootToNode(node,arr,x):
    if not node:
        return False
    arr.append(node.val)
    if node.val ==x:
        return True
    if rootToNode(node.left,arr,x) or rootToNode(node.right,arr,x):
        return True
    arr.pop()
    return False

T = TreeNode()
root = T.insert([1,2,3,4,5])
arr=[]
rootToNode(root, arr, 3)
print(arr)

