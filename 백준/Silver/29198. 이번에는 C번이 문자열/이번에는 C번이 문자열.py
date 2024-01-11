n,m,k=map(int,input().split())
S=[sorted(list(input())) for i in range(n)]
S.sort()
answer=[]
for i in range(k):
    temp=S[i]
    for j in range(m):
        answer.append(temp[j])
print(''.join(sorted(answer)))
