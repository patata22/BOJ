n,m = map(int,input().split())
number= tuple(map(int,input().split()))
now = sum(number[:m])
l=0
r=m-1
answer=now
count=1
while r<n-1:
    r+=1
    now+=number[r]
    now-=number[l]
    l+=1
    if now>answer:
        answer=now
        count=1
    elif now==answer:
        count+=1
if answer==0: print('SAD')
else:
    print(answer)
    print(count)
          
