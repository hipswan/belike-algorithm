from turtle import pos
from binary_tree import TreeNode

def preInPostTraversal(node,pre,ino,post):
    s = []
    
    if node is None:
        return
    
    s.append((node,1))
    while len(s)!=0:
        curr,num = s.pop()
        if num == 1:
            pre.append(curr.val)
            s.append((curr,num+1))
            if curr.left is not None:
                s.append((curr.left,1))
        elif num==2:
            ino.append(curr.val)
            s.append((curr,num+1))
            if curr.left is not None:
                s.append((curr.right,1))
        else:
            post.append(curr.val)
    
    return

T = TreeNode()
root = T.insert([1,2,3,4,5])
pre,ino,post =[] ,[],[]
preInPostTraversal(root,pre,ino,post)
print(pre,ino,post)

