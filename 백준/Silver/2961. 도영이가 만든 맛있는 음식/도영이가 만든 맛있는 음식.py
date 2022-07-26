def sol(cnt,start,sour,bitter):
    global answer
    if cnt==11:    return
    if cnt!=0:answer=min(answer,abs(sour-bitter))
    for i in range(start, n):
        if not used[i]:
            used[i]=1
            s,b= ingredients[i]
            sol(cnt+1, i+1, sour*s, bitter+b)
            used[i]=0
            


n=int(input())
ingredients = [list(map(int,input().split())) for i in range(n)]
used=[0]*n
answer=float('inf')

sol(0,0,1,0)
print(answer)
