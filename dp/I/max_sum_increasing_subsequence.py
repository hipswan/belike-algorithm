# maximum sum increasing subsequence

from cmath import inf
from collections import deque


def maxSumSubsequence(arr):
    n = len(arr)
    dp = [x for x in arr]
    track=[-1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j]+arr[i]
                track[i] = j 
    max_ = -inf
    idx = -1
    for i,sum_ in enumerate(dp):
        if max_ <= sum_:
            idx = i
            max_=sum_
    
    sequence = deque()
    while idx != -1:
        sequence.appendleft(arr[idx])
        idx = track[idx]
    return max_ , sequence

print(maxSumSubsequence([4,6,1,3,8,4,6]))
