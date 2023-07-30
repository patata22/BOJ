def failure(s):
    l=len(s)
    fail=[0]*l
    j=0
    for i in range(1,l):
        while j>0 and s[i]!=s[j]: j=fail[j-1]
        if s[i]==s[j]:
            j+=1
            fail[i]=j
    return fail

def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

n=int(input())
target = input().split()
circle = input().split()
circle.extend(circle[:n-1])

fail=failure(target)
answer=0
j=0
l = len(circle)
for i in range(l):
    while j>0 and circle[i]!=target[j]: j= fail[j-1]
    if circle[i]==target[j]:
        if j==n-1:
            answer+=1
            j=fail[j]
        else: j+=1

g=gcd(answer,n)
print(f'{answer//g}/{n//g}')     