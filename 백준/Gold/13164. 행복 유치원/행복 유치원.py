n,k=map(int,input().split())
number=list(map(int,input().split()))
answer=number[-1]-number[0]
gap=[number[i]-number[i-1] for i in range(1,n)]
gap.sort()
for _ in range(k-1):
    answer-=gap.pop()
print(answer)
