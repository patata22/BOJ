x=list(map(int,input().split()))
x.sort()

c1,c2,c3=map(int,input().split())
if c2>c3: c3,c2=c2,c3
a1=sum(x)*c1/100
a2=(x[-1]*c3+x[-2]*c2)/100
if a1<=a2: print('two', '%.2f' %a2)
else:print('one', '%.2f' %a1)
