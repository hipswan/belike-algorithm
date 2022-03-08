

def powerSet(word):
    n = len(word)
    subs=[]
    for i in range(1<<n):
        sub=""
        for j in range(n):
            if i & (1<<j):
                sub+=word[j]
        subs.append(sub)

    return subs
print(powerSet('pneumono'))
