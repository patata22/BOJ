DIV=10**9+7
def sol(x):
    if x==1:return 2
    temp= sol(x//2)
    if x%2: return ((temp%DIV)*(temp%DIV)*2)%DIV
    else: return ((temp%DIV)*(temp%DIV))%DIV

n=int(input())
if n<=1: print(1)
else:print(sol(n-1))
