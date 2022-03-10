# there are memoization and tabulation method both with same TC-->O(mn)
# Here I have shown optimized tabulation with SC-->O(n) instead of O(mn)

from cmath import inf


def minimumSumPath(grid=[]):
    # rows 
    m = len(grid)
    n = len(grid[0])
    prev = [inf]*n
    for i in range(m):
        curr = [0]*n
        for j in range(n):
            if i==0 and j==0:
                curr[j] = grid[i][j]
            else:
                up = grid[i][j]+prev[j]
                left= grid[i][j]
                if j>0:
                    left+=curr[j-1]
                else:
                    left+=inf
                curr[j] = min(up,left)
        prev =curr
    return prev[n-1]    

print(minimumSumPath([[1,3,1],[2,3,2],[4,3,1]]))