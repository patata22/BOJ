def change(i):
    x=n
    cnt=0
    while x:
        cnt+=x%i
        x//=i
    return cnt

n=int(input())

answer=0
answer2=0
for i in range(2,n+1):
    result=change(i)
    if result>answer:
        answer=result
        answer2=i
    answer=max(answer,change(i))
print(answer,answer2)
