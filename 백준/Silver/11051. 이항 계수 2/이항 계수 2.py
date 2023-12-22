answer=1
n,k=map(int,input().split())
k=min(k,n-k)
for i in range(1,k+1):
    answer*=n-i+1
    answer//=i
print(answer%10007)
    
