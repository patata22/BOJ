n,m=map(int,input().split())
friend=[[0]*n for i in range(n)]
for i in range(n): friend[i][i]=1
day=2
cnt=n
for _ in range(m):
    a,b=map(lambda x: int(x)-1,input().split())
    friend[a][b]=1
    friend[b][a]=1
    cnt+=2

answer=[]
while cnt<n*n:
    temp=0
    for i in range(n):
        for j in range(n):
            if 1<=friend[i][j]<day:
                for k in range(n):                    
                    if not friend[i][k] and 1<=friend[j][k]<day:
                        friend[i][k]=day
                        temp+=1
    
    day+=1
    answer.append(temp//2)
    cnt+=temp

print(day-2)
for x in answer:print(x)
