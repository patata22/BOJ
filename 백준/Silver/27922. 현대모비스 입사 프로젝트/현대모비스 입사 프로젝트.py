def sol(a,b):
    temp=0
    number.sort(key=lambda x: -x[a]-x[b])
    for i in range(k):
        temp+=number[i][a]+number[i][b]
    return temp

n,k=map(int,input().split())
number=[tuple(map(int,input().split())) for i in range(n)]
answer=0
for i in range(3):
    for j in range(i+1,3):
        answer=max(answer,sol(i,j))
print(answer)
