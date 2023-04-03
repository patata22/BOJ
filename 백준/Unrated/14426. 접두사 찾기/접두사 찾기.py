import sys
input=sys.stdin.readline

def insert(s):
    global unused
    now=1
    for x in s:
        char = charToInt(x)
        if nxt[now][char]==-1:
            nxt[now][char]=unused
            unused+=1
        now=nxt[now][char]

def isPrefix(s):
    now=1
    for x in s:
        char = charToInt(x)
        if nxt[now][char]==-1:
            return 0
        now=nxt[now][char]
    return 1
    
def charToInt(x):
    return ord(x)-97


n,m=map(int,input().split())

MAX = 5000005
nxt=[[-1]*26 for i in range(MAX)]
unused=2
answer=0
for _ in range(n):
    insert(input().rstrip())

for _ in range(m):
    answer+=isPrefix(input().rstrip())
print(answer)
