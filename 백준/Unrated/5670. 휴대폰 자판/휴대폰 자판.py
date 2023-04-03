import sys
input=sys.stdin.readline

def charToInt(x):
    return ord(x)-97

def insert(s):
    global unused
    now=1
    for x in s:
        char=charToInt(x)
        if char not in nxt[now]:
            count[now]+=1
            nxt[now][char]=unused
            unused+=1
        now=nxt[now][char]
    count[now]+=1
            
def find(s):    
    now=1
    t=0
    if len(nxt[now])==1:t+=1
    for x in s:
        if count[now]!=1: t+=1
        char=charToInt(x)
        now=nxt[now][char]
    return t

while True:
    try:
        n=int(input())
        unused=2
        MAX = 10**6+1
        nxt=[{} for i in range(MAX)]
        count=[0]*MAX
        answer=0

        words=[input().rstrip() for i in range(n)]
        for word in words: insert(word)
        for word in words: answer+=find(word)
        print(f'{round(answer/n + 0.0001,2):.2f}')
    except: break
