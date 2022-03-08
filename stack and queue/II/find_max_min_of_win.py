# find maximum of minimum of sliding window of size k
from collections import deque
from curses import window
from xml.etree.ElementPath import find


def findMaxMinofWindows(nums=[],windowSize=0):
    n = len(nums)
    res =[]
    if n*windowSize == 0:
        return res
    if windowSize <=0:
        return res
    q = deque()
    for i,num in enumerate(nums):
        if q and q[0] == i - windowSize:
            q.popleft()
        while q and num < nums[q[0]]:
            q.pop()
        q.append(i)
        if i >=windowSize-1:
            res.append(nums[q[0]])
    return max(res)

print(findMaxMinofWindows(nums=[1,2,3,5,6],windowSize=3))
 