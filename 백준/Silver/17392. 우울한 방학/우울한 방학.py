n,m=map(int,input().split())
for x in map(int,input().split()):
    m-=x+1
if m<=0: print(0)
else:
    base,add=divmod(m,n+1)
    answer=(n+1)*(base*(base+1)*(2*base+1))//6
    answer+=add*((base+1)**2)
    print(answer)
