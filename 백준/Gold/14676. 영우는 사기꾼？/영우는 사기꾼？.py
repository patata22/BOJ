import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
indegree=[0]*(n+1)
built=[0]*(n+1)
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

answer="King-God-Emperor"    
for _ in range(k):
    a,b=map(int,input().split())
    if a==1:
        if indegree[b]!=0:
            answer="Lier!"
            break
        else:
            built[b]+=1
            if built[b]==1:
                for x in graph[b]:
                    indegree[x]-=1
                    
                
    elif a==2:
        built[b]-=1
        if built[b]<0:
            answer="Lier!"
            break
        elif built[b]==0:
            for x in graph[b]:
                indegree[x]+=1
print(answer)
