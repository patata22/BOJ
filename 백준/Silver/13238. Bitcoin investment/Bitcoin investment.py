high=0
low=100001
answer=0

input()
number=list(map(int,input().split()))
while number:
    now=number.pop()
    if now>high:
        high=now
        low=100001
    elif now<low:
        low=now
        answer=max(answer,high-low)
    answer=max(answer,high-low)
print(answer)
