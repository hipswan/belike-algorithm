from binary_tree import TreeNode

def inorderSuccessor(root,p):
    successor = None
    while root:
        if root.val > p.val:
            successor = root
            root  = root.left
        if root.val < p.val:
            root = root.right
        if root.val == p.val:
            break
    return successor


def findpresuc(root,pre,suc,key):
    if not root:
        return
    findpresuc(root.left,pre,suc,key)
    if root.val < key:
        pre = root.val
    if root.val > key and not suc:
        suc = root.val
    findpresuc(root.right,pre,suc,key)



T = TreeNode()
root = T.insert([5,2,7,1,4,6,9,None,None,3])
print(inorderSuccessor(root,TreeNode(val=3)))