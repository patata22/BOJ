import sys
input=sys.stdin.readline

n,k=map(int,input().split())
ice=[tuple(map(int,input().split())) for i in range(n)]
ice.sort(key=lambda x: x[1])

l=0
r=0
answer=ice[0][0]
total=ice[0][0]
while r<n-1:
    r+=1
    total+=ice[r][0]
    
    while ice[r][1]-ice[l][1]>2*k:
        total-=ice[l][0]
        l+=1
    answer=max(answer,total)
print(answer)
