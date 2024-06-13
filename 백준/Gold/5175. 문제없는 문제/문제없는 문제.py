def sol(depth):
    global total,answer
    if depth==n:
        if len(temp)<total:
            for i in range(1,m+1):
                if not used[i]: return
            total=len(temp)
            answer=temp[:]
        return
    for x in problem[depth]:
        used[x]+=1
    temp.append(depth)
    sol(depth+1)
    for x in problem[depth]:
        used[x]-=1
    temp.pop()
    sol(depth+1)

for tt in range(int(input())):
    if tt: print()
    m,n=map(int,input().split())
    problem=[tuple(map(int,input().split())) for i in range(n)]
    used=[0]*(m+1)
    total=float('inf')
    temp=[]
    answer=[]
    sol(0)
    answer=map(lambda x: chr(x+65),answer)
    print(f'Data Set {tt+1}:',end=' ')
    print(*answer)
    
    
