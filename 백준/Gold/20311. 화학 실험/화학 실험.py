n,k=map(int,input().split())
number=sorted(list(enumerate(map(int,input().split()))),key=lambda x: -x[1])
m=0
for x,y in number:
    m=max(m,y)
answer=[0]*n
if (n%2==0 and m>n//2) or (n%2 and m>n//2+1):print(-1)
else:
    idx=0
    count=0
    for i in range(0,n,2):
        if count==number[idx][1]:
            idx+=1
            count=0
        answer[i]=number[idx][0]+1
        count+=1
    for i in range(1,n,2):
        if count==number[idx][1]:
            idx+=1
            count=0
        answer[i]=number[idx][0]+1
        count+=1
    print(*answer)
