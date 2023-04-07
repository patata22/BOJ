n=int(input())
price=list(map(int,input().split()))
stack=[price.pop()]
answer=0
while price:
    now=price.pop()
    if stack[-1]>now: answer=max(answer,stack[-1]-now)
    else: stack.append(now)
print(answer)
