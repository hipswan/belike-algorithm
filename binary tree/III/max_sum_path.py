from binary_tree import TreeNode

def max_sum_path(root,maxi):
    if root is None:
        return 0
    left = max_sum_path(root.left,maxi)
    right = max_sum_path(root.right,maxi)
    maxi[0] = max(maxi[0] , root.val + left + right)
    return root.val + max(left,right)


T = TreeNode()
root = T.insert([1,2,3])
maxi = [0]
max_sum_path(root,maxi)
print(maxi[0])