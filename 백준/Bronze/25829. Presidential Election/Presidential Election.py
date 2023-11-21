left=0
right=0
totalL=0
totalR=0
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if b>c:left+=a
    else: right+=a
    totalL+=b
    totalR+=c

if left>right and totalL>totalR:print(1)
elif left<right and totalL<totalR:print(2)
else: print(0)
    
