n=int(input())
answer=0
number=0
odd=[]
while number<n:
    temp=list(map(int,input().split()))
    number+=len(temp)
    for x in temp:
        if x%2: odd.append(x)
        answer+=x
odd.sort()
if len(odd)%2:
    answer-=odd[0]
print(answer//2)