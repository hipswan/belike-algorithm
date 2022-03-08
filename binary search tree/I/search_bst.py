from binary_tree import TreeNode

def searchInBST(root,val):
    if root is None or root.val == val :
        return root
    if val<root.val:
        searchInBST(root.left)
    else:
        searchInBST(root.right)
    

T = TreeNode()
root = T.insert([8,5,12,4,7,10,14,None,6,None,None,None,13])
print(searchInBST(root))