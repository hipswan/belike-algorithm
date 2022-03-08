from cmath import inf
def kthElementSortedArray(nums1,nums2,n,m,k):
    if n>m:
        return kthElementSortedArray(nums2,nums1,m,n,k)
    low = max(0,m-k)
    high = min(n,k)
    while low<=high:
        cut1 = low + (high-low>>1)
        cut2 = k - cut1
        left1 = nums1[cut1-1] if cut1!=0 else -inf
        left2 = nums2[cut2-1] if cut2!=0 else -inf
        right1 = nums1[cut1] if cut1!=n else inf
        right2 = nums2[cut2] if cut2!=m else inf
        if left1<=right2 and left2<=right1:
            return max(left1,left2)
        elif left1>right2:
            high=cut1-1
        else:
            low=cut1+1
    return 1


print(kthElementSortedArray([8,12,14,15],[1,2,3,4,9,11],4,6,5))