n=int(input())
now='1'

while n-len(now)>0:
    n-=len(now)
    now=str(int(now)+1)
print(now[n-1])
