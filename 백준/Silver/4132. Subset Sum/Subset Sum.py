def sol(depth,total):
    if depth==m:
        global answer
        if total>=n and total-n<answer-n:
            answer=total
        return
    sol(depth+1,total+number[depth])
    sol(depth+1,total)

n,m=map(int,input().split())
number=[int(input()) for i in range(m)]
answer=float('inf')
sol(0,0)
print(answer) if answer!=float('inf') else print('IMPOSSIBLE')
