import sys
input=sys.stdin.readline

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

count={}
n=int(input())
for _ in range(n):
    a,b,c=map(int,input().split())
    g=gcd(a,b)
    a//=g
    b//=g
    minus=False
    if a*b<0: minus=True
    a=abs(a)
    b=abs(b)
    if minus:
        if (-a,b) not in count: count[(-a,b)]=0
        count[(-a,b)]+=1
    else:
        if (a,b) not in count: count[(a,b)]=0
        count[(a,b)]+=1

n=(n*(n-1))//2
for x in count:
    m=count[x]
    n-=(m*(m-1)//2)
print(n)
