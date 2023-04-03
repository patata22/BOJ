import sys
input=sys.stdin.readline

def charToInt(x):
    return ord(x)-97

def insert(s):
    global unused
    now=1
    for x in s:
        char=charToInt(x)
        if nxt[now][char]==-1:
            nxt[now][char]=unused
            unused+=1
        now=nxt[now][char]
    check[now]+=1

def find(s):
    now=1
    for x in s:
        char=charToInt(x)
        if nxt[now][char]==-1:
            return False
        now=nxt[now][char]
    return bool(check[now])

def erase(s):
    now=1
    for x in s:
        char=charToInt(x)
        if nxt[now][char]==-1:
            return
        now=nxt[now][char]
    check[now]-=1
    
n,m=map(int,input().split())        
unused=2
MAX= n*500+5

nxt=[[-1]*26 for i in range(MAX)]
check=[0]*MAX

answer=0
for _ in range(n):
    insert(input().rstrip())

for _ in range(m):
    answer+=find(input().rstrip())

print(answer)
    
