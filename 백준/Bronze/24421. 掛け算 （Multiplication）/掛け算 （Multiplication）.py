n=int(input())
number=list(map(int,input().split()))
answer=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if number[i]*number[j]==number[k]: answer+=1
print(answer)