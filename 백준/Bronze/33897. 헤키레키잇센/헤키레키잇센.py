n=int(input())
number=tuple(map(int,input().split()))
streak=1
answer1=1
answer2=1
for i in range(1,n):
    if number[i]>=number[i-1]: streak+=1
    else:
        answer1+=1
        answer2=max(answer2,streak)
        streak=1

answer2=max(answer2,streak)
print(answer1,answer2)
