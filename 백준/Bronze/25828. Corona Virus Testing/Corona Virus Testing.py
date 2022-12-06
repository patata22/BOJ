g,p,t= map(int,input().split())

total = g*p
group = g+t*p
if total==group:print(0)
elif total>group:print(2)
else:print(1)


