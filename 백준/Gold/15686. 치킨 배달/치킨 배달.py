def sol(start,cnt):
    global answer
    if cnt==m:
        temp_total=0
        for i,j in house:
            temp = float('inf')
            for k in range(len(chicken)):
                if used[k]:
                    x,y=chicken[k]
                    temp = min(temp, abs(x-i)+abs(y-j))
                    
            temp_total+=temp
        answer=min(temp_total, answer)
        return
    for i in range(start,len(chicken)):
        if not used[i]:
            used[i]=1
            sol(i+1,cnt+1)
            used[i]=0


n,m=map(int,input().split())
house=[]
chicken=[]
answer=float('inf')
for i in range(n):
    x=list(map(int,input().split()))
    for j in range(n):
        if x[j]==1:house.append((i,j))
        elif x[j]==2:chicken.append((i,j))
used=[0]*len(chicken)
sol(0,0)
print(answer)
