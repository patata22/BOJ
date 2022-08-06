n,k=map(int,input().split())
exp=0
stone=sorted(list(map(int,input().split())))
for i in range(k):
    exp+=i*stone[i]
for i in range(k,n):
    exp+=k*stone[i]

print(exp)
