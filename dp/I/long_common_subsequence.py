# longest common subsequence

def lCS(str1 , str2):
    m = len(str1)
    n = len(str2)
    lcs = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    idx = lcs[-1][-1]
    commonStrArr = ["-"]*idx
    i=m
    j=n
    while i > 0 and j>0:
        if str1[i-1] == str2[j-1]:
            commonStrArr[idx-1] = str1[i-1]
            idx-=1
            i-=1
            j-=1
        elif lcs[i-1][j] == lcs[i][j]:
            i-=1
        else:
            j-=1
    return str1,str2,''.join(commonStrArr)

print(lCS('AGGTAB', 'GXTXAYB'))