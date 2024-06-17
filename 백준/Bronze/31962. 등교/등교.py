n,t=map(int,input().split())
answer=-1

for _ in range(n):
    s,e=map(int,input().split())
    if s+e<=t:
        answer=max(answer,s)
print(answer)

