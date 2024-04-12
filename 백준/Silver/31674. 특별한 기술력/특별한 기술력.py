DIV=10**9+7

n=int(input())
number=sorted(list(map(int,input().split())))
answer=number[-1]
total=0
while number:
    grow=(total+number.pop())%DIV
    total=(total+grow)%DIV

print(total%DIV)
    
