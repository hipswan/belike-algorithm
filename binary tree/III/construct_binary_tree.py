from binary_tree import TreeNode


def construct_binary_tree(indorder , preorder,prestart,preend,instart,inend,inMap):
    if prestart > preend or instart > inend:
        return
    root = TreeNode(val=preorder[prestart])
    inRoot = inMap[root.val]
    numsleft = inRoot  - instart

    root.left = construct_binary_tree(inorder,preorder,prestart+1,prestart+numsleft,instart, inRoot-1,inMap)
    root.right = construct_binary_tree(inorder,preorder,prestart+numsleft+1,preend,inRoot+1, inend,inMap)
    return root




T = TreeNode()
inorder = [2,1,3]
preorder = [1,2,3]
#hash inorder array to find loc 
dict_ = {}
for i in range(len(inorder)):
    dict_[inorder[i]] = i

root = T.insert([1,2,3])
maxi = [0]
root = construct_binary_tree(inorder,preorder,0,len(preorder)-1,0,len(inorder)-1,dict_)
