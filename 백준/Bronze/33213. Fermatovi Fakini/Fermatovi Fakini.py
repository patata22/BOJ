n=int(input())

number=set(map(int,input().split()))
odd=0
even=0
for x in number:
    if x%2: odd+=1
    else: even+=1

if odd>even:
    for i in range(1,1000001,2):
        if i not in number:
            print(i)
            break
else:
    for i in range(2,1000001,2):
        if i not in number:
            print(i)
            break
