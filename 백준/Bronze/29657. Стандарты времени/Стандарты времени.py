h,m,s=map(int,input().split())
a,b,c=map(int,input().split())
t1,t2,t3=map(int,input().split())
total= t1*(m*s)+t2*s+t3
total%=a*b*c
H=b*c
h=total//H
total%=H
m=total//c
s=total%c
print(h,m,s)