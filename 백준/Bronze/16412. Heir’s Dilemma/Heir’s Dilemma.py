def change(x):
    y=x
    temp=set()
    while y:
        temp.add(y%10)
        y//=10
    if 0 in temp or len(temp)!=6: return 0
    for a in temp:
        if x%a: return 0
    return 1

a,b=map(int,input().split())

answer=0
for i in range(a,b+1):
    answer+=change(i)
print(answer)
