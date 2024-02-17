n,k=map(int,input().split())
number=list(map(int,input().split()))
answer=[0]*n
m=max(number)
if (n%2==0 and m>n//2) or (n%2 and m>n//2+1):print(-1)
else:
    idx=0
    for i in range(0,n,2):
        if not number[idx]:
            idx+=1
        answer[i]=idx+1
        number[idx]-=1
    for i in range(1,n,2):
        if not number[idx]:
            idx+=1
        answer[i]=idx+1
        number[idx]-=1
    print(*answer)
        
                
