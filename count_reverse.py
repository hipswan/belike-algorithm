def merge(low,mid,high,nums):
    count = 0
    j = mid+1
    for i in range(low,mid+1):
        while( j<=high and nums[i]>2*nums[j]):
            j+=1
        count+=j-(mid+1)
    
    arr=[]
    left = low
    right = mid+1
    while(left<=mid and right<=high):
        if(nums[left] <= nums[right]):
            arr.append(nums[left])
            left+=1
        else:
            arr.append(nums[right])
            right+=1

    while(left<=mid):
        arr.append(nums[left])
        left+=1
    
    while(right<=high):
        arr.append(nums[right])
        right+=1
    
    for i in range(low,high+1):
        nums[i] = arr[i - low]

print(merge(0,0,1,[3,2]))

