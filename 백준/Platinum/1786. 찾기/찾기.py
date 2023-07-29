def failure(s):
    f = [0]*len(s)
    j = 0
    for i in range(1,len(s)):
        while j>0 and s[i]!=s[j]: j= f[j-1]
        if s[i]==s[j]:
            j+=1
            f[i]=j
    return f

a = list(input())
b = list(input())
N=len(a)
M=len(b)
f = failure(b)
j=0
answer=[]
for i in range(N):
    while j>0 and a[i]!=b[j]: j = f[j-1]
    if a[i] == b[j]:
        if j==M-1:
            answer.append(i-M+2)
            j=f[j]
        else: j+=1

print(len(answer))
for x in answer:print(x)