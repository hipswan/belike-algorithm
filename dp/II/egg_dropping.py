# Egg Dropping

from cmath import inf


def eggDropping(egg,floors):
    
    dp=[[0 for _ in range(floors+1)] for _ in range(egg+1)]
    for i in range(egg+1):
        for j in range(floors+1):
            if i == 0:
                dp[i][j]=None
            elif j ==0:
                dp[i][j] =0
            elif j==1:
                dp[i][j] =1
            elif i == 1:
                dp[i][j] = j
            else:
                min_ = inf
                for k in range(j-1,-1,-1):
                    # egg survives
                    v1 = dp[i][k]
                    # egg breaks
                    v2 = dp[i-1][(j-1)-k]
                    min_ = min(max(v1,v2),min_)
                dp[i][j] = min_ +1
    
    return dp[-1][-1]

print(eggDropping(3,7))