class Stack():
    def __init__(self):
        self.arr=[]
        self.top = -1
    
    def push(self,n):
        self.top+=1
        self.arr.append(n)
    
    def pop(self):
        self.top-=1
        return self.arr[self.top+1]
    
    def len(self):
        return self.top+1
    
    def isEmpty(self):
        return self.top==-1

s = Stack()
s.push(3)
s.push(3)
print(s.pop(),s.isEmpty())


