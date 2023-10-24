import sys
input=sys.stdin.readline

x,y,m=map(int,input().split())
M=m
damage = [int(input()) for i in range(x)]
heal = [int(input()) for i in range(y)]

damage=list(enumerate(damage))
damage.sort(key=lambda x: x[1], reverse=True)

heal=list(enumerate(heal))
heal.sort(key=lambda x: x[1], reverse=True)
flag=True
answer=[]
for i,d in damage: 
    if d>=m:
        while m<=d:
            if not heal:
                flag=False
                break
            j,x=heal.pop()
            answer.append(j+1)
            m=min(m+x,M)
    m-=d
    answer.append(-i-1)
while heal:
    answer.append(heal.pop()[0]+1)
if not flag:print(0)
else:print(*answer,sep='\n')
        
    
    
