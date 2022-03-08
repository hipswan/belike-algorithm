
from binary_tree import TreeNode


def leftview(node,level,arr):
    if node is None:
        return
    if level == len(arr):
        arr.append(node.val)
    leftview(node.left,level+1,arr)
    leftview(node.right,level+1,arr)

T = TreeNode()
root = T.insert([1,2,3,4,5])
arr = []
leftview(root,0,arr)
print(arr)

