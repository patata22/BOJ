import sys
input=sys.stdin.readline

total=0
n=int(input())
color=[0]*(n+1)
ball=[[i,*map(int,input().split())] for i in range(n)]
answer=[0]*n

ball.sort(key=lambda x: x[2])
before=-1
temp={}
for idx,c,size in ball:
    if before!=size:
        for x in temp:
            color[x]+=temp[x]
            total+=temp[x]
        temp.clear()
    answer[idx]=total-color[c]
    if c in temp: temp[c]+=size
    else: temp[c]=size
    before=size

print(*answer,sep='\n')
