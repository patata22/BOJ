def sol(now,total,depth):
    global answer
    if total==k:
        answer+=1
        return
    for i in range(now+1, n):
        a,b,c=table[i]
        if a==5: continue
        if total+c-b+1>k: continue
        flag=True
        for j in range(b,c+1):
            if visited[a][j]: flag=False
        if not flag: continue
    
        
        for j in range(b,c+1):
            visited[a][j]=1
        sol(i, total+c-b+1,depth+1)
    
        for j in range(b,c+1):
            visited[a][j]=0
            
            

n,k=map(int,input().split())
table=[]
for i in range(n):
    a,b,c=map(int,input().split())
    table.append((a,b,c))
visited=[[0]*11 for i in range(5)]
answer=0
sol(-1,0,0)
print(answer)
