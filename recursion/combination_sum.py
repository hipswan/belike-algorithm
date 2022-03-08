def combinationSum2(candidates, target: int):
    sum_arr = []
    candidates.sort()
    findCombinationSum2(0, candidates, target, [], sum_arr)
    return sum_arr


def findCombinationSum2(index, candidates, target, arr, sum_arr):
    if target == 0:
        sum_arr.append(list(arr))
        return
    for i in range(index, len(candidates)):
        if i != index and candidates[i] == candidates[i-1]:
            continue
        if candidates[i] > target:
            break
        arr.append(candidates[i])
        findCombinationSum2(index+1, candidates, target -
                            candidates[i], arr, sum_arr)
        arr.remove(candidates[i])

print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))