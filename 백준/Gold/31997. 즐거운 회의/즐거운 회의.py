import sys
input=sys.stdin.readline

n,m,t=map(int,input().split())
start=[0]*n
end=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    start[i]=a
    end[i]=b

answer=[0]*(t+2)

for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    s=max(start[a],start[b])
    e=min(end[a],end[b])
    if s<e:
        answer[s]+=1
        answer[e]-=1

for i in range(1,t):
    answer[i]+=answer[i-1]
answer.pop()

print('\n'.join(map(str,answer[:t])))