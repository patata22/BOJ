import sys
input=sys.stdin.readline
def gcd(x,y):
    while y:
        x,y= y,x%y
    return x
    
A,d=map(int,input().split())
a=A
number=[0]*1000001
number[1]=a
for i in range(2,1000001):
    a+=d
    number[i]+=a+number[i-1]
g=gcd(A,d)


for _ in range(int(input())):
    q,l,r=map(int,input().split())
    if q==1:
        print(number[r]-number[l-1])
    else:
        if l==r: print(A+(l-1)*d)
        else:print(g)
        
        
