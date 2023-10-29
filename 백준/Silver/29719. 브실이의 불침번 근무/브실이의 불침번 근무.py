DIV=10**9+7
def power(x,y):
    if x==0: return 1
    if x==1: return y
    temp=power(x//2,y)
    if x%2==1:return temp*temp*y%DIV
    else: return temp*temp%DIV
    

n,m=map(int,input().split())
print((power(n,m)%DIV-power(n,m-1)%DIV)%DIV)
