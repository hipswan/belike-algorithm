# Number of Islands

def dfs(m,n,i,j,region):
    region[i][j] = 2
    dx = [0,0,-1,1]
    dy=[1,-1,0,0]
    for k in range(4):
        if i+dy[k] < m and i+dy[k] >= 0 and j+dx[k] < n and j+dx[k] >=0 and region[i+dy[k]][j+dx[k]] == 1:
            dfs(m,n,i+dy[k],j+dx[k],region)

def numberOfIslands(region):
    # rows
    m=len(region)
    # columns
    n = len(region[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if region[i][j] not in [0,2]:
                dfs(m,n,i,j,region)
                count+=1

    for i in range(m):
        for j in range(n):
            if region[i][j]==2:
                region[i][j]=1      
    return count

region1 = [ [1,1,1,1] , [1,0,0,1] , [1,0,0,0] ]
region2 = [ [1,1,0,1] , [0,0,1,0] , [0,0,0,0] ]

print(numberOfIslands(region1))


