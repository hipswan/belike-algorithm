def subsets(nums):
    sum_arr = []
    findSubset(0, [], nums, sum_arr)
    return sum_arr


def findSubset(index, sum_, arr, sum_arr):

    if index == len(arr):
        sum_arr.append(sum_)
        return
    print(sum_)
    findSubset(index+1, sum_+[arr[index]], arr, sum_arr)
    findSubset(index+1, sum_, arr, sum_arr)


def subsetsWithDup(nums):
    nums.sort()
    subset_arr = []
    findSubsetWithDuplicate(0, nums, [], subset_arr)
    return subset_arr


def findSubsetWithDuplicate(index, nums, arr, subset_arr):
    subset_arr.append(list(arr))
    for i in range(index, len(nums)):
        if i != index and nums[i] == nums[i-1]:
            continue
        arr.append(nums[i])
        findSubsetWithDuplicate(i+1, nums, arr, subset_arr)
        arr.remove(nums[i])

print(subsets([1,2,3]))
print(subsetsWithDup([1,2,2]))