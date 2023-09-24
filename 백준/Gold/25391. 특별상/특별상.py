import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
answer=0
score=[]
for _ in range(n):
    a,b=map(int,input().split())
    score.append([a,b,1])
    
score.sort(key=lambda x: x[1])
temp=[]
for _ in range(k):
    a,b,c=score.pop()
    answer+=a
    temp.append([a,b,0])
for x in temp: score.append(x)
score.sort(key=lambda x: (x[0],x[2]))
cnt=0
while cnt<m:
    a,b,c=score.pop()
    if not c: continue
    cnt+=1
    answer+=a
print(answer)
