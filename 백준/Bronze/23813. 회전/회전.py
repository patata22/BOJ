number=list(map(int,list(input())))
l = len(number)
answer=0
total = sum(number)
now=1
for i in range(l):
    answer+=total*now
    now*=10
print(answer)
