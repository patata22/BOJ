n=int(input())
X=list(map(int,input().split()))
L=list(map(int,input().split()))
C=input().split()
answer=[]
for i in range(n):
    if answer:break
    for j in range(i+1,n):
        if abs(X[i]-X[j])<=L[i]+L[j] and C[i]!=C[j]:
            answer.append((i+1,j+1))
if answer:
    print('YES')
    print(*answer[0])
else:print('NO')
