from collections import deque
def segment(x, space):
    # Write your code here
    n = len(space)
    q = deque()
    res = []
    i=0
    while i< n:
        if q and q[0] == i - x:
            q.popleft()
        while q and space[q[-1]] > space[i]:
            q.pop()
        q.append(i)
        if i >=x-1:
            res.append(space[q[0]])
        i+=1
    return max(res)

print(segment(3,[1,2,3,4,5]))

# TC-->O(n) + O(n)(amotized as there are n element)
# SC-->O(k)
