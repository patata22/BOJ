x1,x2=map(int,input().split())
a,b,c,d,e=map(int,input().split())
a//=3
b//=2
d//=2
b-=d
c-=e
print(-(a*(x1**3-x2**3)+b*(x1**2-x2**2)+c*(x1-x2)))