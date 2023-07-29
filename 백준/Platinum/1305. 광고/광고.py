def failure(s):
    l=len(s)
    fail = [0]*l
    j=0
    for i in range(1,l):
        while j>0 and s[i]!=s[j]: j=fail[j-1]
        if s[i]==s[j]:
            j+=1
            fail[i]=j
    return fail

n=int(input())
fail = failure(list(input()))
print(n-fail[-1])
