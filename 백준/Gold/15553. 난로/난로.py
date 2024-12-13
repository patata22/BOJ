import sys
input=sys.stdin.readline

n,k=map(int,input().split())
time=[int(input()) for i in range(n)]
gap=[]
for i in range(1,n):
    gap.append(time[i]-time[i-1]-1)
gap.sort()
answer=time[-1]-time[0]+1
for _ in range(k-1):
    if not gap: break
    answer-=gap.pop()
print(answer)
