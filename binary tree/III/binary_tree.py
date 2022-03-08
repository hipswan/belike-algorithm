
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self,arr,root=None,idx=0):
        
        if idx < len(arr):
            if arr[idx] is None:
                return None
            root = TreeNode(val=arr[idx])
            root.left = self.insert(arr,root.left, 2*idx+1)
            root.right = self.insert(arr,root.right, 2*idx+2)
        return root

T = TreeNode()
root = T.insert([1,2,3,None,None,5,6,None,None,None,None,7,8])
