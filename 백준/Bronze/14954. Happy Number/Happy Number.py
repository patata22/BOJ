def change(x):
    total=0
    while x:
        total+=(x%10)**2
        x//=10
    return total

n=int(input())
answer='HAPPY'
record=set()
record.add(n)
while n!=1:
    n=change(n)
    if n in record:
        answer='UNHAPPY'
        break
    record.add(n)

print(answer)