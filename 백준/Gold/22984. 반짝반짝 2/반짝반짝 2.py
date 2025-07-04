n=int(input())
number=list(map(float,input().split()))
answer=sum(number)
for i in range(1,n):
    p,q=number[i-1],number[i]
    answer+=p*(1-q)+q*(1-p)
print(answer)
