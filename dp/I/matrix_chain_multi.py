# matrix chain multiplication

from cmath import inf
from collections import namedtuple

def printMatrix(i,j,matrices,brackets,name,chainStr):
    if i == j:
        # print(name[0],sep='')
        chainStr.append(matrices[name[0]])
        name[0]+=1
        # name[0] = chr(ord(name[0])+1)

        return
    # print("(" , sep='')
    chainStr.append('(')


    printMatrix(i,brackets[i][j],matrices,brackets,name,chainStr)
    printMatrix(brackets[i][j]+1,j,matrices,brackets,name,chainStr)
    chainStr.append(")")



def matrixChainMultiplication(matrices):
    n = len(matrices)
    dp = [[0 for i in range(n)] for j in range(n)]
    brackets = [[0 for i in range(n)] for j in range(n)]
    for l in range(1,n):
        for i in range(n-l):
            j = i+l
            dp[i][j] = inf
            for k in range(i,j):
                q =  dp[i][k]+dp[k+1][j]+ matrices[i].rows*matrices[k].cols*matrices[j].cols
                if q<dp[i][j]:
                    dp[i][j] = q
                    brackets[i][j] = k
    chainStr = []
    printMatrix(0,n-1,matrices,brackets,[0],chainStr)

    return dp[0][n-1],chainStr
    



Matrix = namedtuple('Matrix' ,'rows cols')
matrices = [Matrix(2,3),Matrix(3,6),Matrix(6,4),Matrix(4,5)]
print(matrixChainMultiplication(matrices))