n=int(input())+1

weight=[0]+list(map(int,input().split()))
energy=[0]+list(map(int,input().split()))
dp=[0]*n

for i in range(1,n): 
    cost=float('inf')
    w_max=0
    e_max=0
    for j in range(i,0,-1):
        w_max=max(w_max,weight[j])
        e_max=max(e_max,energy[j])
        cost=min(cost,dp[j-1]+w_max*e_max)
    dp[i]=cost

print(dp[-1])