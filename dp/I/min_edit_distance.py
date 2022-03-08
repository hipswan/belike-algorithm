# minimum edit distance
# from str1 -- > str2
from collections import deque


def minEditDistance(str1,str2):
    m = len(str1)
    n = len(str2)
    dist = [[None for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        dist[i][0] = i
    for j in range(n+1):
        dist[0][j] = j
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = min(dist[i-1][j-1],dist[i][j-1],dist[i-1][j]) + 1

    editSequence =deque()
    i = m
    j = n
    while True:
        if i ==0 or j == 0:
            break
        elif str1[i-1] == str2[j-1]:
            i-=1
            j-=1
        elif dist[i][j] == dist[i-1][j-1] + 1:
            editSequence.appendleft(f"edit {str2[j-1]} in string 2 to {str1[i-1]} in string 1")
            i-=1
            j-=1
        elif dist[i][j] == dist[i][j-1]+1:
            editSequence.appendleft(f"delete in string 2 {str2[j-1]}")
            j-=1
        elif dist[i][j] == dist[i-1][j]+1:
            editSequence.appendleft(f"delete in string 1 {str1[i-1]}")
            i-=1
        else:
            print("Error Occurred")
            break
    
    return editSequence



print(minEditDistance('azced','abcdef'))
