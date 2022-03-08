# there are two methods one with tc --> O(n^2) and other with tc--> O(nlogn)




from cmath import inf
from collections import deque


def lIS(arr):
    n = len(arr)
    dp = [1] * n
    track=[-1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j]+1
                track[i] = j 
    max_ = -inf
    idx = -1
    for i,len_ in enumerate(dp):
        if max_ <= len_:
            idx = i
            max_=len_
    
    sequence = deque()
    while idx != -1:
        sequence.appendleft(arr[idx])
        idx = track[idx]
    return max_ , sequence

def ceilIndex(arr, low,high,key):
    while low<high:
        mid = low + ((high -low)>>1)
        if arr[mid][0] >= key:
            high = mid
        else:
            low = mid+1
    return high


def lIS_2(arr):
    n = len(arr)
    tail = [(0,0)]*n
    tail[0] = arr[0],0
    len_ = 1
    track=[-1]*n
    for i in range(1,n):
        if arr[i] < tail[0][0]:
            tail[0] = arr[i],i
        elif arr[i] > tail[len_-1][0]:
            tail[len_] = arr[i],i
            track[i] = tail[len_-1][1]
            len_+=1
        else:
            idx = ceilIndex(tail,0,len_-1,arr[i])
            tail[idx] = arr[i],i
            track[i] = tail[idx-1][1]
    idx = tail[len_ - 1][1]
    sequence = deque()
    while idx != -1:
        sequence.appendleft(arr[idx])
        idx = track[idx]
    return len_ , sequence


print(lIS_2([3,4,-1,0,6,2,3]))
# print(ceilIndex([1,3,4,5,6] , 0 ,4,5))


