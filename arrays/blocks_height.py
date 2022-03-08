from cmath import inf
import math
def blockHeight(blocks,height):
    n = len(blocks)
    width = math.ceil(sum(blocks) / height)
    mark =0 
    mini_ = -inf
    for i in range(n):
        if mark+blocks[i] <=width:
            mark+=blocks[i]
        else:
            
            mark = blocks[i]
        mini_ = max(mark,mini_)
    return mini_

print(blockHeight([1,3,1,3,3] , 2))
