import sys
input=sys.stdin.readline


X=int(input())
n=int(input())
limit=X//20
score=[]
answer={}
for i in range(n):
    name, v = input().split()
    v=int(v)
    if v<limit: continue
    answer[name]=0
    

    for j in range(1,15):
        score.append((name,v//j))

score.sort(key= lambda x: -x[1])
for i in range(14):
    answer[score[i][0]]+=1

for x in sorted([(x,answer[x]) for x in answer],key=lambda x: x[0]): print(*x)

