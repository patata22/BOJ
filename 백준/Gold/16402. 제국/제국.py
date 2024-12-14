import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    pa,pb=find(a),find(b)
    if pa!=pb:
        p[pb]=pa
    else:
        if pa!=a:
            p[a]=-1
            p[b]=a


n,m=map(int,input().split())
p=[-1]*n
nameToNum={}
numToName={}

for i in range(n):
    name=input().rstrip()
    nameToNum[name]=i
    numToName[i]=name

for _ in range(m):
    a,b,c=input().split(',')
    c=int(c)
    a=nameToNum[a]
    b=nameToNum[b]
    if c==1: union(a,b)
    else: union(b,a)

temp=[]
for i in range(n):
    if p[i]<0: temp.append(i)

answer=[]
for x in temp:
    answer.append(numToName[x])
answer.sort()
print(len(answer))
for x in answer: print(x)
        