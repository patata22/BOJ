def sol():
    MAX=-float('inf')
    target=0
    for i in range(n):
        for j in range(n):
            if j in check: continue
            if common[i]*team[j]>MAX:
                target=j
                MAX=common[i]*team[j]
    check.add(target)
    return MAX
                

n,k=map(int,input().split())
common=tuple(map(int,input().split()))
team=tuple(map(int,input().split()))
check=set()
for _ in range(k):sol()
print(sol())
