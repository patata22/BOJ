import sys

def insert(s):
    global unused,answer
    now=1
    for x in list(map(int,list(s))):
        if nxt[now][x]==-1:
            nxt[now][x]=unused
            unused+=1
        now=nxt[now][x]
        if check[now]:
            answer='NO'
            return

    if sum(nxt[now])!=-10: answer='NO'
    check[now]=1        

for _ in range(int(input())):
    answer='YES'

    n=int(input())
    MAX= n*10+5
    unused=2
    
    nxt=[[-1]*10 for i in range(MAX)]
    check=[0]*MAX

    string=[input().rstrip() for i in range(n)]

    for s in string:
        insert(s)

    print(answer)
