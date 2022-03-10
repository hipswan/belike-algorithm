# word break
# we will set dp[len(s)+1] to true as it is the last string and can be 
# splited ( this does not make sense)
# 
def wordBreak(s,wordDict):
    n = len(s)
    dp = [0]*(n+1)
    dp[n]=True
    for i in range(n-1,-1,-1):
        for word in wordDict:
            if i + len(word)<=n and s[i:i+len(word)] == word:
                dp[i] = dp[i + len(word)]
    return dp[0]
print(wordBreak("leetcode",["leet","code"]))