a,b=map(int,input().split())
d=int(input())
total= (100*a+b)//2
total-=d

x=total//2+d
y=total//2
print(*divmod(x,100))
print(*divmod(y,100))
