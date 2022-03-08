


def matrixMedian(matrix):
    low = 1
    high = int(1e9)
    m=len(matrix)
    n=len(matrix[0])
    while low<=high:
        mid = low+(high-low>> 1)
        count=0
        for i in range(n):
            count+=countNumbersLessThanMid(matrix[i],mid)
        if count <=(n*m>>1):
            low=mid+1
        else:
            high=mid-1
    return low
def countNumbersLessThanMid(arr,num):
    low=0
    high=len(arr)-1
    while low<=high:
        mid = low+(high-low>>1)
        if arr[mid] <= num:
            low=mid+1
        else:
            high=mid-1
    return low

print(matrixMedian([[1,3,6],[2,6,9],[3,6,9]]))