def toThree(n):
    answer=""
    while n:
        answer+=str(n%3)
        n//=3
    if not answer:return 0
    return int(answer[::-1])

x,y=map(int,input().split())
X=toThree(x)
Y=toThree(y)

total = X+Y
answer=1

while total:
    if total%10!=1:
        answer=0
        break
    total//=10

print(answer)