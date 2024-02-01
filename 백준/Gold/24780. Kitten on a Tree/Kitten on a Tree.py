k=int(input())

def makeTree(now):
    for to in graph[now]:
        parent[to]=now
        makeTree(to)

parent=[0]*101
graph=[[] for i in range(101)]
indegree=[0]*101
outdegree=[0]*101

while True:
    number=list(map(int,input().split()))
    if number[0]==-1: break
    a=number[0]
    for i in range(1,len(number)):
        b=number[i]
        graph[a].append(b)
        indegree[b]+=1
        outdegree[a]+=1

for i in range(1,101):
    if not indegree[i] and outdegree[i]:
        root=i
makeTree(root)

while k:
    print(k, end=' ')
    k=parent[k]
