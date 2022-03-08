class Queue():
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.count = 0
        self.arr = [0]*size

    def push(self,n):
        if self.count==self.size:
            return -1
        elif self.rear==-1:
            self.rear = 0
            self.front = 0
        else:
            self.rear=(self.rear+1) % self.size
        self.arr[self.rear] = n
        self.count+=1
    
    def pop(self):
        if self.count == 0:
            return -1
        front = self.front
        if self.count==1:
            self.front = -1
            self.rear = -1   
        else:
            self.front=(self.front+1)%self.size
        self.count-=1
        return self.arr[front%self.size]
        
    def top(self):
        return self.arr[self.front%self.size]

    def size(self):
        return self.count

q = Queue(5)

print(q.size)