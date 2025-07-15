for tt in range(int(input())):
    number=list(map(int,input().split()))
    answer=[]
    while len(number)>1:
        a,b=divmod(number.pop(),2)
        number[-1]+=a
        answer.append(b)
    answer.append(number.pop())
    print(*answer[::-1])
