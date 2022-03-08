class Node:
    def __init__(self):
        self.links = {}
        self.cntEndWith = 0
        self.cntPrefix = 0
        self.flag = False
    
    def containsKey(self,char):
        return self.links.get(ord(char) - ord('a')) != None
    
    def get(self,char):
        return self.links.get(ord(char)-ord('a'))
    
    def put(self,char):
        self.links[ord(char)-ord('a')] = Node()
    
    def increaseEnd(self):
        self.cntEndWith+=1
    def increasePrefix(self):
        self.cntPrefix+=1

    def deleteEnd(self):
        self.cntEndWith-=1
    
    def reducePrefix(self):
        self.cntPrefix-=1
    
    def getEnd(self):
        return self.cntEndWith
    
    def getPrefix(self):
        return self.cntPrefix

    def isEnd(self):
        return self.flag
class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self,word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i])
            node=node.get(word[i])
            node.increasePrefix()
        node.increaseEnd()
        node.flag = True
    
    
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

    def countWordsEqualTo(self,word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return 0
            else:
                node = node.get(word[i])
        
        return node.getEnd()
    
    def erase(self,word):
        node = self.root
        for i in range(len(word)):
            if node.containsKey(word[i]):
                node=node.get(word[i])
                node.reducePrefix()
            else:
                return
        node.deleteEnd()
    
    def countWordsStartingWith(self,word):
        node=self.root
        for i in range(len(word)):
            if node.containsKey(word[i]):
                node=node.get(word[i])
            else:
                return 0

        return node.getPrefix()

    def checkIfPrefixExist(self,word):
        node = self.root
        flag = True
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return False
            else:
                node=node.get(word[i])
                flag = node.isEnd()
            if not flag:
                return False
        return flag

    def countDistinctSubstring(self,word):
        count = 0 
        for i in range(len(word)):
            node = self.root
            for j in range(i,len(word)):
                if not node.containsKey(word[j]):
                    node.put(word[j])
                    count+=1
                node = node.get(word[j])
        
        return count+1
T = Trie()

words=['n','ni','nin','ninj','ninja','ninga']
for word in words:
    T.insert(word)

longest = ""
for word in words:
    if T.checkIfPrefixExist(word):
        if len(word) > len(longest):
            longest = word
        elif len(word) == len(longest):
            if word > longest:
                longest = word
print(longest)