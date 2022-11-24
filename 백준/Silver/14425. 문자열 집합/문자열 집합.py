import sys
input=sys.stdin.readline

dic={}
n,m=map(int,input().split())
for _ in range(n):
    x=input().rstrip()
    dic[x]=0
answer=0
for _ in range(m):
    x=input().rstrip()
    if x in dic:answer+=1
print(answer)
