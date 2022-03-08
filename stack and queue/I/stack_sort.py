def stackinsert(stack , x):
    if len(stack)==0 or x>=stack[-1]:
        stack.append(x)
        return
    tmp = stack.pop()
    stackinsert(stack,x)
    stack.append(tmp)
def sortstack(stack):
    if len(stack) !=0:
        x = stack.pop()
        sortstack(stack)
        stackinsert(stack,x)

print(sortstack([4,3,2,1]))
