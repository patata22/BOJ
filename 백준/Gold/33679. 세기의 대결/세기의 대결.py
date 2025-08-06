from collections import deque

def check(number):
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if number[i]>number[j]: dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

n=int(input())
number1=deque(map(int,input().split()))
number2=deque(map(int,input().split()))
answer1=0
answer2=0
for i in range(n):
    answer1=max(answer1,check(number1))
    answer2=max(answer2,check(number2))
    number1.append(number1.popleft())
    number2.append(number2.popleft())


if answer1==answer2: print('Both Win!')
elif answer1>answer2: print('YJ Win!')
else: print('HG Win!')
