from binary_tree import TreeNode

def sameTree(p,q):
    if p is None or q is None:
        return p==q
    return p.val == q.val and sameTree(p.left,q.left) and sameTree(p.right,q.right)

T = TreeNode()
p = T.insert([1,2,3,4,5,6,8,9])
q = T.insert([1,2,3,4,5,6,7,8,9])

print(sameTree(p,q))