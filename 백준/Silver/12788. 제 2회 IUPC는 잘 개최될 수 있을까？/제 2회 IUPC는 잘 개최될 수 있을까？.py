n=int(input())
m,k=map(int,input().split())
total=m*k
answer=0
number=list(map(int,input().split()))
if sum(number)<total: print("STRESS")
else:
    number.sort()
    pen=0
    while pen<total:
        pen+=number.pop()
        answer+=1
    print(answer)
