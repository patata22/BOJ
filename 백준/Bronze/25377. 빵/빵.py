answer=float('inf')
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<=b:answer=min(answer,b)
print(-1) if answer==float('inf') else print(answer)
    
