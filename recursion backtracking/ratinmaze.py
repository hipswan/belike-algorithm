def ratInMaze(m, n):
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    vis = [[0 for i in range(n)] for i in range(n)]
    ans = []
    if m[0][0] == 1:
        findRatInMaze(0, 0, m, n, ans, "", vis, di, dj)
    return ans


def findRatInMaze(i, j, m, n, ans, move, vis, di, dj):
    if i == n-1 and j == n-1:
        ans.append(move)
        return
    dir = "DLRU"
    for ind in range(4):
        nexti = i+di[ind]
        nextj = j+dj[ind]
        if(nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and vis[nexti][nextj] != 1 and m[nexti][nextj]):
            vis[i][j] = 1
            findRatInMaze(nexti, nextj, m, n, ans, move+dir[ind], vis, di, dj)
            vis[i][j] = 0

print(ratInMaze([[1,  0,  0,  0], 
 [1  ,1  ,0 , 0 ],
 [0 , 1,  0,  0], 
 [0,  1,  1,  1]],4))