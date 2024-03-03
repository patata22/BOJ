from collections import deque
import sys
input=sys.stdin.readline

START=0
END=301

def makeFlow():
    total=0
    while True:
        q=deque()
        q.append(START)
        prev=[-1]*302
        while q:
            now=q.popleft()
            for to in graph[now]:
                if prev[to]==-1 and capa[now][to]>0:
                    prev[to]=now
                    q.append(to)
                    if to==END: break
        if prev[-1]==-1: break

        total+=1
        now=END
        while now!=START:
            capa[prev[now]][now]-=1
            capa[now][prev[now]]+=1
            now=prev[now]
    return total                

n,k,d=map(int,input().split())
graph=[[] for i in range(302)]
capa=[[0]*302 for i in range(302)]

for i in range(1,n+1):
    graph[0].append(i)
    graph[i].append(0)
    capa[0][i]=k

foodLimit=list(map(int,input().split()))
for i in range(d):
    num=i+201
    graph[num].append(END)
    graph[END].append(num)
    capa[num][END]=foodLimit[i]

for people in range(1,n+1):
    foods=list(map(int,input().split()))[1:]
    for food in foods:
        graph[people].append(food+200)
        graph[food+200].append(people)
        capa[people][food+200]=1
          
print(makeFlow())