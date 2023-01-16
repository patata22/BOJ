n=int(input())
number=tuple(map(int,input().split()))

now=number[0]
answer=now
for i in range(1,n):
    if number[i]==now+1:
        now+=1
    else:
        now=number[i]
        answer+=now
print(answer)
