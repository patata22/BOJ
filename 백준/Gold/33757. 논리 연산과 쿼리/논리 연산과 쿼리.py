n,q=map(int,input().split())

ori=input().split('|')
query=tuple(map(lambda x: int(x)-1,input().split()))

result=0
idx=0
length=[0]*len(ori)
total=[0]*len(ori)
value={}
group={}

for i in range(len(ori)):
    y=ori[i]
    length[i]=len(y)//2+1
    temp=0
    for x in y:
        if x=='&': continue
        if x=='0': value[idx]=0
        elif x=='1':
            value[idx]=1
            total[i]+=1
            temp+=1
        group[idx]=i
        idx+=1
    if temp==length[i]:
        result+=1
        total[i]=temp
        
answer=[]

for x in query:
    g=group[x]
    if value[x]==0:
        value[x]=1
        total[g]+=1
        if total[g]==length[g]: result+=1
    else:
        if total[g]==length[g]: result-=1
        total[g]-=1
        value[x]=0
    if result: answer.append('1')
    else: answer.append('0')

print(''.join(answer))
