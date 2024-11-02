import sys
input=sys.stdin.readline

n,d,k,c=map(int,input().split())

dish=[0]*(d+1)
dish[c]=1

number=[int(input()) for i in range(n)]

for i in range(k):
    number.append(number[i])
n=len(number)
now=1
answer=0
for i in range(k):
    if not dish[number[i]]:now+=1
    dish[number[i]]+=1
l=0
r=k-1
while r+1<n:
    r+=1
    if not dish[number[r]]:now+=1
    dish[number[r]]+=1
    dish[number[l]]-=1
    if not dish[number[l]]:now-=1
    l+=1
    answer=max(answer,now)

print(answer)
