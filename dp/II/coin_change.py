# coin change
# infinite supply of coins and we have to return the minimum 
# number of coins require to add up to given amount
# tc-->O(n*k), where k = len(coins)
# sc--> O(n)
from cmath import inf


def coinChange(coins=[],amount=0):
    dp = [amount+1]*(amount+1)
    dp[0]=0
    for  i in range(1,amount+1):
        for coin in coins:
            if i - coin >=0:
                dp[i] = min(dp[i],1 + dp[i-coin])
    return dp[-1] if dp[-1] !=amount+1 else -1

print(coinChange(coins=[1,3,4,5],amount=222209213))