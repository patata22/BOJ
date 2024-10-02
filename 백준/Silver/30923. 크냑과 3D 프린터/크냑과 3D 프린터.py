n=int(input())
number=list(map(int,input().split()))

answer=2*sum(number)+2*n
for i in range(n-1):
    answer+=abs(number[i]-number[i+1])
answer+=number[0]+number[-1]
print(answer)

