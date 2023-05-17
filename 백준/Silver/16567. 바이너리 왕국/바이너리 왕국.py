import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=list(map(int,input().split()))
answer=0
now=-1
for x in number:
    if x==1 and x!=now:
        answer+=1
    now=x

for _ in range(m):
    temp=list(map(int,input().split()))
    if temp[0]==0:
        print(answer)
    else:
        x=temp[1]-1
        if number[x]==1: continue
        else:
            flag=0
            number[x]=1
            for i in (-1,1):
                if 0<=x+i<n and number[x+i]==1:
                    flag+=1
            if flag==0: answer+=1
            elif flag==2: answer-=1
            
        
