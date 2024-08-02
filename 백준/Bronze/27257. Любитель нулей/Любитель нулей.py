n=int(input())
while not n%10: n//=10
answer=0
while n:
    if not n%10:answer+=1
    n//=10
print(answer)
