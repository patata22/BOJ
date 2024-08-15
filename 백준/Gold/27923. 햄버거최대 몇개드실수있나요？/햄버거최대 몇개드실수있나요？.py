n,k,l=map(int,input().split())
hamburger=list(map(int,input().split()))
coke=list(map(int,input().split()))

prefix=[0]*(n+1)

for x in coke:
    prefix[x]+=1
    if x+l<=n: prefix[x+l]-=1

for i in range(1,n+1):
    prefix[i]+=prefix[i-1]

hamburger.sort()
prefix.sort()
two={}
for x in prefix:
    if x not in two:
        two[x]=2**x
answer=0
while hamburger:
    answer+=int(hamburger.pop()/(two[prefix.pop()]))

print(answer)