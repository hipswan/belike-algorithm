# maximum job scheduling
# same time means not overlap
from typing import List

def binarySearch(arr,lo=0,startIdx=0):
    hi = startIdx-1
    while lo <= hi:
        mid = lo + ((hi-lo) >>1)
        if arr[mid][1] <= arr[startIdx][0]:
            if arr[mid+1][1]<= arr[startIdx][0]:
                lo = mid+1
            else:
                return mid
        else:
            hi = mid -1
    
    return -1

def jobScheduling( startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
    n = len(jobs)
    dp = [0 for _ in range(n)]
    dp[0] = jobs[0][2]
    for i in range(1,n):
        val = jobs[i][2]
        l=binarySearch(jobs,0,i)
        if l!=-1:
            val+=dp[l]
        dp[i] = max(val,dp[i-1])

    return max(dp) if dp else 0

print(jobScheduling([1,2,3,3],
[3,4,5,6],
[50,10,40,70]))