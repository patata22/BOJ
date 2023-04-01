n=int(input())

A=1
for x in map(int,input().split()):A*=x

answer=[]
flag=False

def sol(depth, now):
    global flag
    if flag:return
    if depth==n:
        if now>A:
            flag=True
            print(*answer)
        return
    for i in range(1,10):
        answer.append(i)
        sol(depth+1, now*i)
        answer.pop()

sol(0,1)
if not flag: print(-1)

