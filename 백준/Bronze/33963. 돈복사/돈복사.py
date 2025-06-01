answer=0
now=int(input())

while len(str(now))==len(str(now*2)):
    answer+=1
    now*=2
print(answer)
