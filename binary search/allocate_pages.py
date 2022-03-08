

def allocateMinimumPages(pages,students):
    low = min(pages)
    high = sum(pages)
    while low<=high:
        mid = low+(high-low>>1)
        if canAllocate(pages,mid,students):
            high = mid-1
        else:
            low=mid+1
    return low


def canAllocate(pages,barrier,students):
    student = 0 
    sumOfpages = 0
    for i in range(len(pages)):
        if sumOfpages + pages[i] > barrier:
            student+=1
            sumOfpages=pages[i]
            if sumOfpages>barrier:
                return False
        else:
            sumOfpages+=pages[i]
    if student<students:
        return True
    else:
        return False

print(allocateMinimumPages([12,34,67,90],2 ))