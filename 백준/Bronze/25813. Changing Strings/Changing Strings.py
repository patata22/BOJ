answer=list(input())
n=len(answer)
now='-'
for i in range(n):
    if answer[i]=='U':
        l=i
        break
for i in range(n-1,-1,-1):
    if answer[i]=='F':
        r=i
        break
for i in range(l):
    answer[i]='-'
for i in range(l+1,r):
    answer[i]='C'
for i in range(r+1,n):
    answer[i]='-'
print(''.join(answer))
