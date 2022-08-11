n=int(input())
condo=[tuple(list(map(int,input().split()))) for i in range(n)]
condo.sort()

temp=float('inf')
answer=0
for i in range(n):
    if condo[i][1]<temp:
        temp=condo[i][1]
        answer+=1
print(answer)
