
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self,arr,root=None,idx=0):
        
        if idx < len(arr):
            root = TreeNode(val=arr[idx])
            root.left = self.insert(arr,root.left, 2*idx+1)
            root.right = self.insert(arr,root.right, 2*idx+2)
        return root

