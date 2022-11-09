import sys
input=sys.stdin.readline

n,m=map(int,input().split())
count={}
word=[]
for _ in range(n):
    x=input().rstrip()
    if len(x)>=m:
        if x not in count:
            count[x]=1
            word.append(x)
        else: count[x]+=1

word.sort(key=lambda x: (-count[x], -len(x), x))

for x in word:
    print(x)

