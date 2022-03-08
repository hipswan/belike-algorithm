import math



def search( nums, target) -> int:
    n = len(nums)
   
    if n==0:
        
            return -1
      
    else:
        
        mid = math.floor((n-1)/2)
        # right = (n-mid) -1 
        
        if nums[mid] == target:
            
            return mid
        elif nums[mid] > target:
            return search(nums[:mid],target)
        elif nums[mid] < target:
             b= search(nums[mid+1:],target)
             return -1 if b==-1 else b+mid+1


print(search([-1,0,3,5,9,12],-3))
