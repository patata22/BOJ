import sys
input=sys.stdin.readline

def sol(idx):
    a=len(count[idx])
    b=len(count[idx-1])
    for i in range(a):
        answer.append(count[idx-1][i]+" "+count[idx][i])
    for i in range(b-a):
        answer.append(count[idx-1][a+i]+" "+count[idx][-1])
    
n=int(input())
number=sorted(enumerate(map(int,input().split())), key=lambda x: x[1])
m=number[-1][1]
count=[[] for i in range(m+1)]
for i,x in number:
    count[x].append(str(i+1))

flag=False
for i in range(1,m+1):
    if len(count[i])>len(count[i-1]) or (len(count[i]) and not len(count[i-1])):
        flag=True
        break
if m>1:
    if len(count[-1])==1 and len(count[-2])==1: flag=True
if flag:print(-1)
else:
    answer=[]
    for i in range(1,m+1):sol(i)
    for i in range(1,len(count[-1])):
        answer.append(count[-1][0]+" "+count[-1][i])
    print('\n'.join(answer))