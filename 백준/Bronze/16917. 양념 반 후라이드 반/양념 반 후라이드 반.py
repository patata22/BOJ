a,b,c,x,y=map(int,input().split())
answer=0
if a+b>=2*c:
    z=min(x,y)
    answer+=2*c*z
    x-=z
    y-=z
a=min(a,2*c)
b=min(b,2*c)
print(answer+a*x+b*y)
