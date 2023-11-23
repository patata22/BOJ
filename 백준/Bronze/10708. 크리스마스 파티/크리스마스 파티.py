n=int(input())
m=int(input())
score=[0]*n
target=list(map(int,input().split()))
for i in range(m):
    temp=list(map(int,input().split()))
    t=target[i]
    count=0
    for j in range(n):
        if temp[j]==t:
            count+=1
            score[j]+=1
    score[t-1]+=n-count
print(*score, sep='\n')
