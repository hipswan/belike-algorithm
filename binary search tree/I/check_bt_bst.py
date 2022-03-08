from cmath import inf
from binary_tree import TreeNode
def checkBtisBst(root):
    return isValidBst(root, -inf,inf)

def isValidBst(root,min,max):
    if root is None or root.val is None :
        return True
    if root.val <= min or root.val >= max:
        return False
    return isValidBst(root.left,min,root.val) and isValidBst(root.right,root.val,max)


T = TreeNode()
root = T.insert([13,10,15,7,12,14,17,None,9])
print(checkBtisBst(root))