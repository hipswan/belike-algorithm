def nthRootofNumber(m,n):
    if m==0:
        return 0
    low=1
    high=m
    
    eps = 1e-6
    while high-low > eps:
        mid = low+(high-low)/2
        if multiply(mid,n) < m:
            low=mid
        else:
            high=mid
    return round(low)

def multiply(m,n):
    ans = 1
    for i in range(n):
        ans*=m
    return ans

print(nthRootofNumber(8,3))