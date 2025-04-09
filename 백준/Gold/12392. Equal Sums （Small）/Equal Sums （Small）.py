def sol(depth):
    global left,right,flag
    if flag: return
    if left==right:
        flag=True
        return
    if depth==len(number): return
    sol(depth+1)
    if flag: return
    right-=number[depth]
    used[depth]=2
    sol(depth+1)
    if flag: return
    used[depth]=1
    left+=number[depth]
    sol(depth+1)
    if flag: return
    left-=number[depth]
    used[depth]=0
    right+=number[depth]

for tt in range(1,int(input())+1):
    number=list(map(int,input().split()))[1:]
    right=sum(number)
    left=0
    #0 = right 1 = left 2 = none
    used=[0]*len(number)
    flag=False
    sol(0)
    print(f'Case #{tt}:')
    if not flag:
        print('Impossible')
    else:
        temp1=[]
        temp2=[]
        for i in range(len(number)):
            if used[i]==0: temp1.append(number[i])
            elif used[i]==1: temp2.append(number[i])
        print(*temp1)
        print(*temp2)
