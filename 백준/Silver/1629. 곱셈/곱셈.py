def sol(a,b,c):
    if b in memo: return memo[b]
    temp=sol(a,b//2,c)
    if b%2==0: memo[b]=temp*temp%c
    else: memo[b]=temp*temp*a%c
    return memo[b]

memo={}
a,b,c=map(int,input().split())
memo[1]=a%c
print(sol(a,b,c))
