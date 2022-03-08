class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}
        
    def addNode(self,node):
        tmp = self.head.next
        tmp.prev = node
        self.head.next = node
        node.prev = self.head
        node.next=tmp

    def deleteNode(self,node):
        delnext = node.next
        delprev = node.prev
        delnext.prev = delprev
        delprev.next = delnext
    
    def get(self, key: int) -> int:
        if self.m.get(key):
            res = self.m[key].val
            self.deleteNode(self.m[key])
            self.addNode(Node(key,res))
            self.m[key] = self.head.next
            return res
        return -1
    
    def put(self, key: int, value: int) -> None:
        if self.m.get(key):
            currNode = self.m[key]
            self.deleteNode(currNode)
        elif self.cap == len(self.m):
            # del or my_dict.pop(key,None) delete key and return None if not exist instead of Keyerror
            # In this case it is certain that some key would exits that why I have used del map[key]
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        self.addNode(Node(key,value))
        self.m[key] = self.head.next
