answer=0
n,B,W=map(int,input().split())
b,w=0,0
road=list(input())

l=0
r=-1
while r+1<n:
    r+=1
    if road[r]=='W': w+=1
    else: b+=1
    while b>B:
        if road[l]=='W': w-=1
        else: b-=1
        l+=1
    if w>=W: answer=max(answer,r-l+1)

print(answer)
