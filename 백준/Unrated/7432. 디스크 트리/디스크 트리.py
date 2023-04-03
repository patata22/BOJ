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

def find(s):
    global A
    now=1
    temp=[]
    depth=0
    for x in s:
        if x=='\\':
            if not printed[now]:
                print(' '*depth+''.join(temp))
                printed[now]=1
            temp=[]
            depth+=1
        else: temp.append(x)
        now=nxt[now][x]
    if not printed[now]:
        printed[now]=1
        print(' '*depth+''.join(temp))
        

n=int(input())
unused=2
MAX=40005
nxt=[{} for i in range(MAX)]
printed=[0]*MAX
directories= [input().rstrip() for i in range(n)]
directories.sort(key = lambda x: x.split('\\'))
for directory in directories: insert(directory)

for directory in directories:
    find(directory)
