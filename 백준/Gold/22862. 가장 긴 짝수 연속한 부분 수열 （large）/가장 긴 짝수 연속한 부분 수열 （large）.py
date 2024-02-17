n,k=map(int,input().split())
number=list(map(int,input().split()))
l=0
r=-1
jump=0
answer=0
while r<n-1:
    r+=1
    if number[r]%2:
        jump+=1
    while jump>k:
        if number[l]%2:
            jump-=1
        l+=1
    answer=max(answer,r-l+1-jump)
        
print(answer)
