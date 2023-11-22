n=int(input())
total=0
answer=0
while True:
    answer+=1
    total += (2*answer-1)**2
    if total>n:break
print(answer-1)
