
import math
import os
import random
import re
import sys



#
# Complete the 'pointsBelong' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#  5. INTEGER x3
#  6. INTEGER y3
#  7. INTEGER xp
#  8. INTEGER yp
#  9. INTEGER xq
#  10. INTEGER yq
#
from enum import Enum

class Status(Enum):
    NOT_VALID = 0
    ONLY_P_BELONGS = 1
    ONLY_Q_BELONGS = 2
    P_AND_Q_BELONGS =3
    NEITHER_P_Q =4
    
def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/ 2.0)

def isInside(x1,y1,x2,y2,x3,y3,xp,yp):
    area_ = area(x1,y1,x2,y2,x3,y3)
    area_1 = area(xp,yp,x2,y2,x3,y3)
    area_2 = area(x1,y1,xp,yp,x3,y3)
    area_3 = area(x1,y1,x2,y2,xp,yp)
    if area_==area_1+area_2+area_3:
        return True
    return False

def dist(x1,y1,x2,y2):
    return abs(math.hypot(x2-x1,y2-y1))
        
def checkNonDegenrate(x1, y1, x2, y2, x3, y3):
    ab = dist(x1, y1, x2, y2)
    bc = dist(x2, y2, x3, y3)
    ac= dist(x1, y1, x3, y3)
    if  ((ab + bc)  > ac) and ((bc+ac) >ab) and ((ab + ac) > bc):
        return True
    return False


def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Write your code here
    
    if not checkNonDegenrate(x1, y1, x2, y2, x3, y3):
        return Status.NOT_VALID
    isP = isInside(x1, y1, x2, y2, x3, y3, xp, yp)
    isQ = isInside(x1, y1, x2, y2, x3, y3, xq, yq)
    if isP:
        if isQ:
            return Status.P_AND_Q_BELONGS.name
        return Status.ONLY_P_BELONGS.name
    elif isQ:
        return Status.ONLY_Q_BELONGS.name
    return Status.NEITHER_P_Q.name
    

print(pointsBelong(3,2,4,5,6,7,8,9,3,5))