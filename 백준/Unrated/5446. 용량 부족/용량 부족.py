import sys
input=sys.stdin.readline

def insert(s):
    global unused
    now=1
    for x in s:
        if x not in nxt[now]:
            nxt[now][x]=unused
            unused+=1
        now=nxt[now][x]

def lock(s):
    now=1
    for x in s:
        safe[now]=1
        if x not in nxt[now]: break
        now=nxt[now][x]
    safe[now]=1
        


def delete(s):
    global answer
    now=1
    t=0
    for x in s:
        if deleted[now]:
            return
        if not safe[now]:
            deleted[now]=1
            answer+=1
            return
        now=nxt[now][x]
    if deleted[now]:return
    if not safe[now]:
        deleted[now]=1
        answer+=1
        return
    answer+=1
    
        
        

for _ in range(int(input())):
    n=int(input())
    files=[input().rstrip() for i in range(n)]
    MAX = n*20+5
    nxt=[{} for i in range(MAX)]
    unused=2
    safe=[0]*MAX
    deleted=[0]*MAX
    for file in files: insert(file)

    for _ in range(int(input())):
        lock(input().rstrip())
    answer=0

    for file in files:
        delete(file)

    print(answer)
    
