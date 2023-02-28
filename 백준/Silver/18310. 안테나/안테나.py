n=int(input())
number=sorted(list(map(int,input().split())))
if n%2:
    print(number[n//2])
else:
    print(number[(n//2)-1])