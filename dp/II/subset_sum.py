# subset sum



def subsetSum(nums=[],target=0):
    n=len(nums)
    # dp = [[False for i in range(target+1)] for j in range(n)]
    
    prev = [False for i in range(target+1)]
    curr = [False for i in range(target+1)]
    prev[0] =True
    
    if nums[0] <=target:
        prev[nums[0]] = True
    for i in range(1,n):
        for j in range(1,target+1):
            notTake = prev[j]
            take=False
            if nums[i] <= j:
                take = prev[j-nums[i]]
            curr[j] = take or notTake
        prev=curr
    return prev[-1]

print(subsetSum([2,3,1,1],4))
    