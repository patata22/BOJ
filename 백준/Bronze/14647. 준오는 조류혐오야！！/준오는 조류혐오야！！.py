n,m=map(int,input().split())
row=[0]*n
col=[0]*m
total=0
for i in range(n):
    temp=input().split()
    for j in range(m):
        now=temp[j]
        c=now.count('9')
        row[i]+=c
        col[j]+=c
        total+=c

print(total - max(max(col),max(row)))
