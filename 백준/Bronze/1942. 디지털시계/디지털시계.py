def toSec(x):
    temp=list(map(int,x.split(':')))
    return 3600*temp[0]+60*temp[1]+temp[2]

def check(x):
    h=x//3600
    x%=3600
    m=x//60
    s=x%60
    temp=10000*h+100*m+s
    if temp%3: return 0
    else: return 1
    
for _ in range(3):
    s,e=map(toSec,input().split())
    if e<s: e+=86400
    answer=0
    for i in range(s,e+1):
        answer+=check(i)
    print(answer)
    
    
    
