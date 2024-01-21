def count2(x):
    t=0
    while x%2==0:
        x//=2
        t+=1
    return t
def count3(x):
    t=0
    while x%3==0:
        x//=3
        t+=1
    return t

n=int(input())
number=list(map(int,input().split()))
number.sort(key=lambda x: (count2(x), -count3(x)))
print(*number)
