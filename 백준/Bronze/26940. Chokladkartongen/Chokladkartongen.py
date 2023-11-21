n=int(input())
number=list(map(int,input().split()))
answer=0
for i in range(1,n):
    if number[i]>number[i-1]:answer+=1  
print(answer)