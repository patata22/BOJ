n=int(input())
poll=tuple(map(int,input().split()))

count=0
answer=0
maxcount=0

for i in range(1,n+1):
    temp=poll.count(i)
    if temp>maxcount:
        maxcount=temp
        count=1
        answer=i
    elif temp==maxcount:
        count+=1
if count>1 or answer==0:print('skipped')
else:print(answer)