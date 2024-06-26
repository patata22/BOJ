n=int(input())
number=sorted(list(map(int,input().split())))
one=number[:n//2+n%2]
two=number[n//2+n%2:][::-1]
answer=[]

while one or two:
    if one: answer.append(one.pop())
    if two: answer.append(two.pop())

print(*answer)
