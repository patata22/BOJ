n,c=map(int,input().split())
answer=[0]*(c+1)
for _ in range(n):
    x=int(input())
    for i in range(x,c+1,x):
        answer[i]=1
print(sum(answer))
