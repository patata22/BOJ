import sys
input=sys.stdin.readline

while True:
    n,m=input().split()
    n=int(n)
    if n==0:break
    m=int(''.join(m.split('.')))
    calory=[0]
    price=[0]
    for _ in range(n):
        a,b=input().split()
        calory.append(int(a))
        price.append(int(''.join(b.split('.'))))

    dp=[0]*(m+1)
    for i in range(1,n+1):
        p=price[i]
        c=calory[i]
        for j in range(p,m+1):
            dp[j]=max(dp[j],dp[j-p]+c)
            
    print(dp[-1])
        