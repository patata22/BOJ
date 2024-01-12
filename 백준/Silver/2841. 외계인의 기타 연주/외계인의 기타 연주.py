import sys
input=sys.stdin.readline

n,p=map(int,input().split())
line=[[] for i in range(7)]
answer=0
for _ in range(n):
    a,b=map(int,input().split())
    while line[a] and line[a][-1]>b:
        line[a].pop()
        answer+=1
    if line[a] and line[a][-1]==b:
        continue
    else:
        line[a].append(b)
        answer+=1
print(answer)
        
