n=int(input())
if n==1:print(1)
elif n%2==0 or n%5==0: print(-1)
else:
    now=1
    answer=1
    while now:
        answer+=1
        now=(now*10+1)%n
    print(answer)