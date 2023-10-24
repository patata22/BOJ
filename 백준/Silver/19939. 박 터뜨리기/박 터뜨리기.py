def sol():
    global n
    total= k*(k+1)//2
    if total>n: return -1
    n-=total
    if not n%k: return k-1
    return k

    
n,k=map(int,input().split())
total = k*(k+1)//2
print(sol())
