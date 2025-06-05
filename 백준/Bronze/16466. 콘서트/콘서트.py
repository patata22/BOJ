n=int(input())
number=sorted(list(map(int,input().split())),reverse=True)
now=1
while number:
    if now==number[-1]:
        number.pop()
        now+=1
    else:break
print(now)
