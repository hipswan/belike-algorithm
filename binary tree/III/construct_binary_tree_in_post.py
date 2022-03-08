from binary_tree import TreeNode


def construct_binary_tree(indorder , postorder,poststart,postend,instart,inend,inMap):
    if poststart > postend or instart > inend:
        return
    root = TreeNode(val=postorder[postend])
    inRoot = inMap[root.val]
    numsleft = inRoot  - instart

    root.left = construct_binary_tree(inorder,postorder,poststart,poststart+numsleft-1,instart, inRoot-1,inMap)
    root.right = construct_binary_tree(inorder,postorder,poststart+numsleft,postend-1,inRoot+1, inend,inMap)
    return root

T = TreeNode()
inorder = [2,1,3]
postorder = [2,3,1]
#hash inorder array to find loc 
dict_ = {}
for i in range(len(inorder)):
    dict_[inorder[i]] = i

root = T.insert([1,2,3])
maxi = [0]
root = construct_binary_tree(inorder,postorder,0,len(postorder)-1,0,len(inorder)-1,dict_)
