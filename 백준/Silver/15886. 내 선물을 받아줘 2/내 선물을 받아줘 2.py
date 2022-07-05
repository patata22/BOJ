n=int(input())
board=list(input())
answer=0
visited=[0]*n
for i in range(n):
    if not visited[i]:
        temp_visited=[0]*n
        temp_visited[i]=1
        now=i
        new=True
        while True:
            if board[now]=='E' and now<n-1:
                if not temp_visited[now+1]:
                    temp_visited[now+1]=1
                    now+=1
                else:break
            elif board[now]=='W' and now>0:
                if not temp_visited[now-1]:
                    temp_visited[now-1]=1
                    now-=1
                else:break
        for i in range(n):
            if visited[i] and temp_visited[i]:new=False
            visited[i]=visited[i]|temp_visited[i]
        if new:answer+=1
print(answer)
                    
