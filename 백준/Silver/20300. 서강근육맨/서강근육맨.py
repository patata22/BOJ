n=int(input())
number=sorted(list(map(int,input().split())))
answer=-1
l=0
r=n-1
if n%2:r-=1
while l<r:
    answer=max(answer,number[l]+number[r])
    l+=1
    r-=1
answer=max(number[-1],answer)
print(answer)