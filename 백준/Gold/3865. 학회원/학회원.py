from collections import deque

def sol():
    q=deque()
    visited=[0]*unused
    visited[0]=1
    q.append(0)
    answer=0
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                if not graph[to]:answer+=1
                else:q.append(to)
    return answer
            

while True:
    n=int(input())
    if not n: break
    numMap={}
    graph={}
    unused=0
    for _ in range(n):
        a,b=input().rstrip('.').split(':')
        if a not in numMap:
            numMap[a]=unused
            graph[unused]=[]
            unused+=1
        for x in b.split(','):
            if x not in numMap:
                numMap[x]=unused
                graph[unused]=[]
                unused+=1
            graph[numMap[a]].append(numMap[x])
    print(sol())