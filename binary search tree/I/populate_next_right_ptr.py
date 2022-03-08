from binary_tree import TreeNode

def populateNextRightPointer(root):
    if not root:
        return None
    curr = root
    while curr.left:
        next = curr.left
        while curr:
            curr.left.next = curr.right
            if curr.next is None:
                curr.right.next = None
            else:
                curr.right.next = curr.next.left
            curr = curr.next
        curr = next
    
    return root

T = TreeNode()
root = T.insert([1,2,3,4,5,6,7])
print(populateNextRightPointer(root))