def parse(x):
    h,m=map(int,x.split(":"))
    return 60*h+m

def sol(t):
    temp=set()
    for i in range(n):
        temp.add((time[i]-t*i)%720)
    return len(temp)

n=int(input())
time=[parse(input()) for i in range(n)]

answer=float('inf')
for i in range(720):
    answer=min(answer,sol(i))

print(answer)