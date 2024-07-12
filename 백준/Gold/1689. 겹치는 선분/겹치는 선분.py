import sys
input=sys.stdin.readline

n=int(input())
line=[tuple(map(int,input().split())) for i in range(n)]
temp=[]
for x,y in line:
    temp.append(x)
    temp.append(y)

temp.sort()
unused=0
compress={}

for x in temp:
    if x in compress: continue
    compress[x]=unused
    unused+=1

count=[0]*2000001

for x,y in line:
    x=compress[x]
    y=compress[y]
    count[x]+=1
    count[y]-=1

for i in range(1,n+1):
    count[i]+=count[i-1]

print(max(count))
