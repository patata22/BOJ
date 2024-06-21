n=int(input())
number=list(map(int,input().split()))
pre=[0]*n
pre[0]=number[0]
for i in range(1,n): pre[i]=pre[i-1]+number[i]

answer=0
for i in range(n):
    answer+=(pre[-1]-pre[i])*number[i]
print(answer)

