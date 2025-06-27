import sys
input=sys.stdin.readline

n,m=map(int,input().split())
price={}
answer=0
for _ in range(n):
    a,b=input().split()
    price[a]=int(b)
for _ in range(m):
    a,b=input().split()
    if int(b)*100>price[a]*105:answer+=1
print(answer)
    
