MAX=1000001

n=int(input())
number=list(map(int,input().split()))
exist=[0]*MAX
win=[0]*MAX
lose=[0]*MAX
for x in number:
    exist[x]=1
for x in number:
    for i in range(x+x,MAX,x):
        if exist[i]:
            win[x]+=1
            lose[i]-=1
            
answer=[]
for x in number:
    answer.append(win[x]+lose[x])
print(*answer)