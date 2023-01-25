def sol(now,p):
    if now==n:return

    global answer
    complete=True

    for x in name[now]:
        take[ord(x)-65]+=1
        
    for i in range(26):
        if target[i]>take[i]:
            complete=False
            break
    if complete:
        answer=min(answer, p+price[now])
    if not complete:
        sol(now+1, p+price[now])
    for x in name[now]:
        take[ord(x)-65]-=1
    sol(now+1, p)
        
target=[0]*26
for x in input():
    target[ord(x)-65]+=1

price=[]
name=[]

take=[0]*26
answer=float('inf')
n=int(input())
for _ in range(n):
    a,b = input().split()
    price.append(int(a))
    name.append(b)

sol(0,0)
print(-1) if answer==float('inf') else print(answer)