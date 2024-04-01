def sol():
    for i in range(1,m+1):
        if not used[i]:
            return i
    return 'ESCAPE FAILED'

n,m=map(int,input().split())
used=[0]*(m+1)
for _ in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='O':used[j+1]+=1

print(sol())
    
