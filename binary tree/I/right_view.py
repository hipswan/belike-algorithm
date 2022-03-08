
from binary_tree import TreeNode


def rightview(node,level,arr):
    if node is None:
        return
    if level == len(arr):
        arr.append(node.val)
    rightview(node.right,level+1,arr)
    rightview(node.left,level+1,arr)

T = TreeNode()
root = T.insert([1,2,3,4,5])
arr = []
rightview(root,0,arr)
print(arr)