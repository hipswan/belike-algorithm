# palindrome partitioning
# minimum cut to partion the string into palindrome
from cmath import inf


def palindromePartitioning(s):
    n = len(s)
    dp_bool = [[False for _ in range(n)] for _ in range(n)]
    for g in range(n):
        i =0
        for j in range(g,n):
            if i==j:
                dp_bool[i][j] = True
            elif (i+1) == j:
                dp_bool[i][j] = s[i] == s[j]
            elif i<j:
                dp_bool[i][j] = s[i]==s[j] and dp_bool[i+1][j-1]
            i+=1
    dp = [0]*n
    for j in range(1,n):
        if dp_bool[0][j]:
            dp[j] =0
            continue
        min_ = inf
        for i in range(j,0,-1):
            if dp_bool[i][j] and dp[i-1] < min_:
                    min_ = dp[i-1]
        dp[j] = min_+1
    return dp[n-1]

print(palindromePartitioning('abbccdd'))


