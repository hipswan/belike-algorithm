class Trie:
    def __init__(self):
        self.root=BitNode()

   
    def bitInsert(self,num):
        node = self.root
        for i in range(4,-1,-1):
            bit = (num>>i) & 1
            if not node.containsKey(bit):
                node.put(bit)
                
            node = node.get(bit)

    def getMax(self,num):
        max_ = 0
        node = self.root
        for i in range(4,-1,-1):
            bit = num>>i & 1
            if node.containsKey(1-bit):
                max_ = max_ | (1<<i)
                node = node.get(1-bit)
            else:
                node=node.get(bit)
        
        return max_

class BitNode():
    def __init__(self):
        self.bits = {}
    
    def containsKey(self,bit):
        return self.bits.get(bit) is not None
    
    def put(self,bit):
        self.bits[bit] = BitNode()

    def get(self,bit):
        return self.bits[bit]

T = Trie()

num1 = [2,3]
num2 = [12]
for num in num1:
    T.bitInsert(num)
maxi =0
for num in num2:
    maxi=max(maxi,T.getMax(num))
print(maxi)
