def sol(cnt):
    if cnt==k:
        answer.add(int(''.join(pick)))
        return
    for i in range(n):
        if not used[i]:
            used[i]=1
            pick.append(card[i])
            sol(cnt+1)
            pick.pop()
            used[i]=0
            
n=int(input())
k=int(input())
card=[input() for i in range(n)]
used=[0]*(n+1)
pick=[]
answer=set()
sol(0)
print(len(answer))
