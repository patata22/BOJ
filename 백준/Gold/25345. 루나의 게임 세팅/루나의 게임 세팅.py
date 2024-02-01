def comb(n,k):
    if k*2>n: k = n-k
    head=1
    tail=1
    for i in range(n,n-k,-1):
        head*=i
    for i in range(2,k+1):
        tail*=i
    return head//tail

n,k=map(int,input().split())
input()
temp=2**(k-1)
print(comb(n,k)*temp%1000000007)
