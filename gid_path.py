
def uniquePaths( m: int, n: int) -> int:
        
    dp=[[-1] * (n+1)]*(m+1)
    
    print(dp)
    num = countPaths(0,0,m,n,dp)
    return dp[0][0]
    
def countPaths( i , j , m , n ,dp):
    if i>=m or j >=n:
        return 0
    if (i == m-1) and (j == n-1):
        return 1
    if dp[i][j] !=-1:
        return dp[i][j]
    dp[i][j] = countPaths(i+1,j,m,n,dp)+countPaths(i,j+1,m,n,dp)
    return dp[i][j]

print(uniquePaths(3,7))