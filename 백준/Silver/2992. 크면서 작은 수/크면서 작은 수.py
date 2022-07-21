def sol(cnt):
    global answer
    if cnt==len(n):
        t=int(''.join(temp))
        if t>N:
            answer=min(t,answer)
        return
    for i in range(len(n)):
        if not used[i]:
            used[i]=1
            temp.append(n[i])
            sol(cnt+1)
            temp.pop()
            used[i]=0

n=list(input())
N=int(''.join(n))
used=[0]*len(n)
temp=[]
answer=float('inf')
sol(0)

print(0) if answer==float('inf') else print(answer)
        
