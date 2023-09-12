a,b,c=map(int,input().split('-'))
total = 360*a + 30*(b-1) + (c-1)
total+=int(input())
y=total//360
total%=360
m=total//30+1

d=total%30+1
if m<10: m= '0'+str(m)
if d<10: d = '0'+str(d)
print(y,m,d,sep='-')
