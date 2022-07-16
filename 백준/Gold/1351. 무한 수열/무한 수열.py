import sys
sys.setrecursionlimit(10**6)

def sol(x):
    if x not in memo:
        memo[x]=sol(x//p)+sol(x//q)
    return memo[x]
    
memo={0:1}

n,p,q=map(int,input().split())
print(sol(n))