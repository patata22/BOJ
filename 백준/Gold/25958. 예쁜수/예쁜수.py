def check(i):
    x=i
    total=0
    while x:
        total+=x%10
        x//=10
    if i%total==0: return True
    
    return False
number=[]

for i in range(1,5001):
    if check(i): number.append(i)

n,DIV=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
for x in number:
    for i in range(1,n+1):
        if x<=i:
            dp[i]=(dp[i]+dp[i-x])%DIV

print(dp[-1])