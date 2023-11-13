number=list(map(int,input().split()))
n=len(number)
cut=int(input())
answer=set()
number.sort()
for i in range(n):
    for j in range(i+1,n):
        if number[i]+number[j]==cut:
            answer.add((number[i],number[j]))
for x,y in answer:
    print(x,y)
print(len(answer))                      