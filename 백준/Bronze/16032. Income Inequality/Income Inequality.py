while True:
    n=int(input())
    if not n: break
    number=list(map(int,input().split()))
    answer=0
    avg=sum(number)/n
    for x in number:
        if x<=avg: answer+=1
    print(answer)