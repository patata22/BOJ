n=int(input())
battery=list(map(int,input().split()))
answer=0
cons=0
now=-1
for x in battery:
    if x==now:
        cons+=1
        answer+=1<<cons
    else:
        cons=1
        answer+=2
        now=x
    if answer>=100:
        answer=0
        cons=0
        now=-1
print(answer)
