
def aggressiveCows(stalls,cows):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    while low<=high:
        mid = low+(high-low>>1)
        if canPlaceCows(stalls,cows,mid):
            low = mid+1
        else:
            high = mid-1
    return high 

def canPlaceCows(stalls,cows,mid):
    cow = 1
    loc = stalls[0]
    for i in range(1,len(stalls)):
        if(stalls[i]-loc >=mid ):
            loc=stalls[i]
            cow+=1
        if cow>=cows:
            return True
    return False

print(aggressiveCows([1,2,8,4,9],3))