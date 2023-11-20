def calc(x):
    total=0
    while x:
        total+=x%10
        x//=10
    return total

l=int(input())
d=int(input())
x=int(input())
for i in range(l,d+1):
    if calc(i)==x:
        print(i)
        break
for i in range(d,l-1,-1):
    if calc(i)==x:
        print(i)
        break
