n=int(input())
condo=[tuple(list(map(int,input().split()))) for i in range(n)]
answer=[1]*n
for i in range(n):
    if not answer[i]:continue
    distance, cost = condo[i]
    for j in range(n):
        if (distance>condo[j][0] and cost>=condo[j][1]) or (cost>condo[j][1] and distance>=condo[j][0]):
            answer[i]=0
            break
            
print(sum(answer))
