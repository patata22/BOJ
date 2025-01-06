import sys
input=sys.stdin.readline

def query(x,y):
    print('?',x,y,flush=True)
    return int(input())
        
def sameGroup(g):
    l=len(distance[g])
    for i in range(l):
        x=distance[g][i]
        cnt=0
        for j in range(i+1,l):
            y=distance[g][j]
            result=query(x,y)
            if result==1:
                cnt+=1
                answer.append((x,y))
            if cnt>20: break

                
n=int(input())
distance=[[] for i in range(n+1)]
answer=[]


for i in range(2,n+1):
    dist=query(1,i)
    if dist==1: answer.append((1,i))
    distance[dist].append(i)

for i in range(1,n):
    sameGroup(i)
    prev=distance[i]
    nxt=distance[i+1]
    for p in prev:
        cnt=0
        for nn in nxt:
            if query(p,nn)==1:
                answer.append((p,nn))
                cnt+=1
            if cnt>20: break

print('!',len(answer),flush=True)
for x in answer:
    print(*x,flush=True)

