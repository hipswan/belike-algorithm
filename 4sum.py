from logging import root
from re import A


def fourSum( nums,target):
    n = len(nums)
    sum4=[]
    nums.sort()
    i=0
    j=0
    while i<n:
        j=i+1
        while j < n:
            
            sum2 = nums[i] + nums[j]
            rem_sum = target - sum2
            left = j+1
            right = n-1
            while left<right:
                if nums[left] + nums[right] < rem_sum:
                    left+=1
                elif nums[left] + nums[right] > rem_sum:
                    right-=1
                else:
                    arr = [nums[i] ,nums[j],nums[left],nums[right]]
                    sum4.append(arr)
                    while left<right and nums[left] == arr[2]:
                        left+=1
                    while left<right and nums[right] ==arr[3]:
                        right-=1
            
            while j+1<n and nums[j+1] == nums[j]:
                j+=1
            j+=1
        while i+1<n and nums[i+1] == nums[i]:
            i+=1
        i+=1
    return sum4



def longestSubarraySumZero(nums):
    n=len(nums)
    sum=0
    maxi=0
    dict_={}
    for i in range(n):
        sum+=nums[i]
        if(sum==0):
            #length
            maxi = i+1
        elif( sum in dict_  ):
            maxi=max(maxi,i- dict_[sum])
        else:
            dict_[sum] = i
    
    return maxi

def longestXor(nums,k):
    n=len(nums)
    dict_={}
    xr=0
    cnt=0
    for i in range(n):
        xr^=nums[i]
        if(xr==k):
            cnt+=1
        elif( xr^k in dict_):
            cnt+=dict_[xr^k]
        elif xr in dict_:
            dict_[xr]+=1
        else:
            dict_[xr]=1
    return cnt

def lengthOfLongestSubstring(s: str) -> int:
        dict_={}
        l =0
        r=0
        leng = 0
        n = len(s)
        while l<n and r<n:
            if s[r] in dict_ :
                l = dict_[s[r]]+1
                
                
            dict_[s[r]] = r
            leng=max(leng,r-l+1)
                
               
            r+=1
        return leng

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def arrayToList(arr):
    n = len(arr)
    if n==0:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1,n):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def reverseList(head):
    if head is None:
        return None
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverseNumber(num , c=0):
    if int(num//10) == 0:
        return num%10
    return 10*c+reverseNumber(num%10 ,c+1 ) 

class Node:
    def __init__(self, x=0,next=None,bottom=None):
        self.val = x
        self.next = next
        self.bottom = bottom

def mergeTwoNode( a,  b):
    dummy = Node()
    temp = dummy
    while a and b:
        if a.val<b.val:
            temp.bottom = a
            temp = temp.bottom
            a=a.bottom 
        else:
            temp.bottom = b
            temp = temp.bottom
            b=b.bottom

    if a:
        temp.bottom =a 
    else:
        temp.bottom=b

    return dummy.bottom

def flattenLinkedList( root):
    if not root or not root.next:
        return root
    root.next = flattenLinkedList(root.next)

    root = mergeTwoNode(root,root.next)

    return root




def nMeetingInAroom(start =[] , end=[]):
    #position of the meeting
    arr=[]
    jobs = sorted(zip(start,end,range(len(start))),key=lambda x:x[1])
    prevFinish = jobs[0][1]
    arr.append(jobs[0][2])
    for i in range(1,len(jobs)):
        #ASSUMING SAME FINISH AND START CAN TAKE PLACE
        if jobs[i][0] >= prevFinish:
            arr.append(jobs[i][2])
    
    return arr,len(arr)

def minPlatformRequired(startTime=[],endTime=[]):
    startTime.sort()
    endTime.sort()
    n = len(startTime)
    platform=0
    j=0
    for i in range(n):
        if startTime[i] <= endTime[j]:
            platform+=1
        else:
            platform-=1
            j+=1
    return platform

def coinChange(coins, amount: int) -> int:
    if amount ==0:
        return 0
    
    arr=[]
    n = len(coins)
    for i in range(n-1,-1,-1):
        while amount>=coins[i]:
            amount-=coins[i]
            arr.append(coins[i])
            
    if len(arr) ==0:
        return -1
    return len(arr)

def fractionalKnapsack(weights,profits,knapsack):
    items = sorted(zip(profits,weights),key=lambda x:x[0]/x[1])
    currWeight =0 
    total_profit=0
    for i in range(len(items)):
        if currWeight+items[i][1] <=knapsack:
            currWeight+=items[i][1]
            total_profit+=items[i][0]
        elif knapsack-currWeight > 0:
            total_profit+=(knapsack-currWeight) * items[i][0]/items[i][1]
        else:
            break
    return total_profit


def maxProfitJobsWithDeadlines(jobids,deadlines,profits):
    jobs = sorted(zip(jobids,deadlines,profits), key=lambda x:x[2],reverse=True )
    max_deadline = max(deadlines)
    job_arr = [-1]*max_deadline
    profit=0
    for i in range(len(jobs)):
        if job_arr[jobs[i][1]-1] == -1:
            job_arr[jobs[i][1]-1] = jobs[i][0]
            profit+=jobs[i][2]
        else:
            for j in range(jobs[i][1]-1,-1,-1):
                if job_arr[j]==-1:
                    job_arr[j] = jobs[i][0]
                    profit+=jobs[i][2]
                    break
    return job_arr,profit

print(maxProfitJobsWithDeadlines([1,2,3],[3,2,3],[20,30,50]))
                    
        

root =flattenLinkedList(Node(5,next=Node(1,bottom=Node(2)),bottom=Node(6)))
print(root)


print(reverseNumber(123))
print(reverseList(arrayToList([1,2,3,4,5])))


print(lengthOfLongestSubstring("abba"))
print(longestXor([4,2,2,6,4,6] , 6))

print(longestSubarraySumZero([-1,1,3,2]))






print(fourSum([-1,1,0,0,2,-2], 0))