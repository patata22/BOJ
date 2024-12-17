def sol(a,b,c,d,e,prev,pprev):
    if prev!=-1 and pprev!=-1 and pprev==prev: return 0
    if a==0 and b==0 and c==0 and d==0 and e==0: return 1
    if dp[a][b][c][d][e][prev][pprev]!=-1: return dp[a][b][c][d][e][prev][pprev]

    result=0
    if a>0 and pprev!=0: result+=sol(a-1,b,c,d,e,0,prev)
    if b>0 and pprev!=1: result+=sol(a,b-1,c,d,e,1,prev)                                
    if c>0 and pprev!=2: result+=sol(a,b,c-1,d,e,2,prev)
    if d>0 and pprev!=3: result+=sol(a,b,c,d-1,e,3,prev)
    if e>0 and pprev!=4: result+=sol(a,b,c,d,e-1,4,prev)
    dp[a][b][c][d][e][prev][pprev]=result
    return result
    

dp=[[[[[[[-1]*5 for i in range(5)] for i in range(11)] for i in range(11)] for i in range(11)] for i in range(11)] for i in range(11)]
temp=[0]*5
for i in range(int(input())):
    temp[i]=int(input())
a,b,c,d,e=temp
print(sol(a,b,c,d,e,-1,-1))

