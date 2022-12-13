answer=0
now=0
for _ in range(int(input())):
    time = int(input())
    temp = min(30-now, time)
    if temp*2>=time: answer+=1
    now+=temp
    if now==30:
        now=0

print(answer)
