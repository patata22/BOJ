n,m=map(int,input().split())

number=tuple(map(int,input().split()))
answer=float('inf')
for i in range(n-1):
    answer=min(answer,number[i]+number[i+1])
print(answer*m)
