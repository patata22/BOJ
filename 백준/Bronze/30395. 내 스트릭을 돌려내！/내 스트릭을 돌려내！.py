n=int(input())
number=list(map(int,input().split()))
streak=0
answer=0
for i in range(n):
    if number[i]:
        streak+=1
    elif i>=1 and not number[i-1] and not number[i]:
        answer=max(answer,streak)
        streak=0
answer=max(answer,streak)
print(answer)
