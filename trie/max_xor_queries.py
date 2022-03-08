
from re import S
from collections import deque
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

nums =[5,2,4,6,6,3]
nums.sort()
n=len(nums)
queries=[[12,4],[8,1],[6,3]]
q = len(queries)
queries = sorted(zip(queries,range(q)),key=lambda x:x[0][1])
ind  = 0
ans = [-1]*q

for i in range(q):
    ai = queries[i][0][1]
    xi = queries[i][0][0]
    q_ind = queries[i][1]
    while ind<n and nums[ind] <=ai:
        T.bitInsert(nums[ind])
        ind+=1
    if ind !=0:
        ans[q_ind] = T.getMax(xi)

print(ans)
