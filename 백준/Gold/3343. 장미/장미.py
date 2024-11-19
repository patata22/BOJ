import math

n,a,b,c,d = map(int, input().split())
if (b/a)<(d/c):
    a,b,c,d=c,d,a,b
 
answer=float('inf')
for i in range(c):
    temp=max(0,math.ceil((n-i*a)/c))
    
    answer=min(answer,math.ceil((i*b)+(temp*d)))
    if temp==0: break

print(answer)
