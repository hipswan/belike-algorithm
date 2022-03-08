
# subarray means contiguous elements of array

def maximumProductSubarray(arr):
    currMax,currMin = 1,1
    res = max(arr)
    for i , n in enumerate(arr):
        if n==0:
            currMax,currMin = 1, 1
            continue
        tmp = n * currMax
        currMax = max(n*currMax,n*currMin,n)
        currMin = min(tmp,n*currMin,n)
        res = max(res,currMax)
    
    return res

print(maximumProductSubarray([-1,-2,-3,4]))