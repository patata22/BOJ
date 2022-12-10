n=int(input())
b=list(map(int,input().split()))
answer=0
for i in range(n):
    if b[i]:
        b[i]=0
        answer+=1
        for j in range(i+1, min(i+3,n)):
            b[j] = 1-b[j]
print(answer)