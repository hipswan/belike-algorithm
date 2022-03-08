# 0 1 knapsack

from collections import deque, namedtuple


def _01knapsack(list_,knapsack):
    dp=  [ [0 for i in range(knapsack+1)] for j in range(len(list_))]
    for i,item in enumerate(list_):
        for j in range(knapsack+1):
            if j < item.wt:
                dp[i][j] = dp[i-1][j]
            else:    
                dp[i][j] = max(item.val + dp[i-1][j - item.wt],dp[i-1][j])
    val = dp[-1][-1]
    i = len(dp)-1
    j = len(dp[0])-1
    items = deque()
    while val > 0:
        if val != dp[i-1][j]:
            items.appendleft(list_[i])
            j-=list_[i].wt
            i-=1
            val = dp[i][j]
        else:
            i-=1
    return items

Item = namedtuple('Item' , 'val wt' )

list_of_item= [ Item(1,1) ,Item(4,3) ,Item(5,4), Item(7,5)  ]
print(_01knapsack(list_of_item,7))
