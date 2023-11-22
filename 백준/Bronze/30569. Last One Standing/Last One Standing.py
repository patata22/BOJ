h1,d1,t1=map(int,input().split())
h2,d2,t2=map(int,input().split())
a=(h2-1)//d1*t1
b=(h1-1)//d2*t2

if a<b:print('player one')
elif a>b: print('player two')
else:print('draw')
