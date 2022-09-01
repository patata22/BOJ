def sol(start, cnt):
    global answer
    if cnt==3:
        score=[0]*n
        for x in choice:
            for y in range(n):
                score[y]=max(score[y],like[y][x])
        answer=max(sum(score),answer)
        return
    for i in range(m):
        choice.append(i)
        sol(i+1, cnt+1)
        choice.pop()

n,m=map(int,input().split())
like=[tuple(map(int,input().split())) for i in range(n)]
choice=[]
answer=0

sol(0,0)
print(answer)