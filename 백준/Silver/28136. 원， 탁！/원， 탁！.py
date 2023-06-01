n=int(input())
number=tuple(map(int,input().split()))
answer=0
for i in range(1,n):
    if number[i]<=number[i-1]:answer+=1
if number[0]<=number[-1]:answer+=1
print(answer)
