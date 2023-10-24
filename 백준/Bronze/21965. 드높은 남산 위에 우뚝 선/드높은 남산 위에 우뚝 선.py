n=int(input())
number=list(map(int,input().split()))
up=True
count=0
answer='YES'
for i in range(1,n):
    if number[i]==number[i-1]: answer='NO'
    if up:
        if number[i]<number[i-1]:
            if count: answer='NO'
            else:
                count=1
                up=False
    else:
        if number[i]>number[i-1]:
            answer='NO'
print(answer)
