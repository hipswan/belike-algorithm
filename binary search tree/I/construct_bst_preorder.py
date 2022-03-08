from cmath import inf
from binary_tree import TreeNode
def constructBstPreorder(arr,i,max_):
    if i[0] == len(arr) or arr[i[0]] > max_:
        return None
    root = TreeNode(val = arr[i[0]])
    i[0] +=1
    root.left = constructBstPreorder(arr,i,root.val)
    root.right = constructBstPreorder(arr,i,max_)
    return root




T = TreeNode()
preorder = [8,5,1,7,10]
print(constructBstPreorder(preorder, [0] ,inf))