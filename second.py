
def isBadVersion(pivot):
    return True if pivot==4 else False

def firstBadVersion( n):
    """
    :type n: int
    :rtype: int
    """
    num=n
   
    bad=0
    pivot = int(n/2)
    while pivot<n:
        

       
        if( isBadVersion(pivot)):
            if bad<pivot:
                bad = pivot
            pivot = pivot/2
        else:
            pivot =int(pivot + (n-pivot)/2 +1)
            
    return bad


n = 5
firstBadVersion(n)