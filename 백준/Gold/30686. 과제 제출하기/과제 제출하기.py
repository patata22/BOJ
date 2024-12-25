import sys
input=sys.stdin.readline

def sol(depth, value):
    if depth==m:
        global answer
        answer=min(answer,value)
        return
    for i in range(m):
        if not solved[i]:
            solved[i]=1
            temp=[]
            knowledge=need[i-1]
            cnt=0
            for x in knowledge:
                if start[x]+limit[x]-1<depth:
                    temp.append((x,start[x]))
                    cnt+=1
                    start[x]=depth
            sol(depth+1,value+cnt)
            for idx,original in temp:
                start[idx]=original
            solved[i]=0
    

n,m=map(int,input().split())
limit=list(map(int,input().split()))
need=[list(map(lambda x: int(x)-1, input().split()))[1:] for _ in range(m)]
solved=[0]*m
start=[-1000]*n
answer=float('inf')
sol(0,0)
print(answer)
