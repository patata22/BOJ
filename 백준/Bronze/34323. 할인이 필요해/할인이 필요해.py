n,m,s=map(int,input().split())
N=((100-n)*s*(m+1)//100)
print(min(N,m*s))