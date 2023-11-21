n=int(input())
number=list(map(int,input().split()))
answer=0
for i in range(n):
    count=1
    now=number[i]
    for j in range(i+1,n):
        if now<number[j]:
            count+=1
            now=number[j]
        else:
            answer=max(answer,count)
            break
    answer=max(answer,count)
print(answer)
