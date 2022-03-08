from binary_tree import TreeNode

def diameter_tree(root,diameter):
    if root is None:
        return 0
    left = diameter_tree(root.left,diameter)
    right = diameter_tree(root.right,diameter)
    diameter[0] = max(diameter[0],left+right)
    return 1+max(left,right)

T = TreeNode()
root = T.insert([1,2,3,4,5,6,7,8,9])
diameter = [0] 
diameter_tree(root,diameter)
print(diameter[0])