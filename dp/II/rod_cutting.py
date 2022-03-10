# rod cutting dp: subsequences

from cmath import inf


def rodCutting(prices=[],rod=0):
    dp= [[0 for i in range(rod+1)] for j in range(rod)]
    for i in range(rod+1):
        dp[0][i] = i*prices[0]
    for i in range(1,rod):
        for j in range(0,rod+1):
            notTake= dp[i-1][j]
            take=-inf
            rodLength = i+1
            if rodLength<=j:
                take = prices[i] + dp[i][j-rodLength]
            dp[i][j] = max(notTake,take)
    
    return dp[-1][-1]

def rodCutting2Array(prices=[],rod=0):
    prev = [0 for i in range(rod+1)]
    curr = [0 for i in range(rod+1)]

    for i in range(rod+1):
        prev[i] = i*prices[0]
    for i in range(1,rod):
        for j in range(0,rod+1):
            notTake= prev[j]
            take=-inf
            rodLength = i+1
            if rodLength<=j:
                take = prices[i] + curr[j-rodLength]
            curr[j] = max(notTake,take)
        prev=curr
    return prev[-1]

def rodCutting1Array(prices=[],rod=0):
    prev = [0 for i in range(rod+1)]

    for i in range(rod+1):
        prev[i] = i*prices[0]
    for i in range(1,rod):
        for j in range(0,rod+1):
            notTake= prev[j]
            take=-inf
            rodLength = i+1
            if rodLength<=j:
                take = prices[i] + prev[j-rodLength]
            prev[j] = max(notTake,take)
    return prev[-1]



print(rodCutting1Array([2,5,7,8,10],5))