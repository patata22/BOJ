n,k=map(int,input().split())
total=0
for _ in range(k):
    total+=int(input())

t=n-k
print((total-3*t)/n, (total+3*t)/n)
