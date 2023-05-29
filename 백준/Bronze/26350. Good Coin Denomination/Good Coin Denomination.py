for _ in range(int(input())):
    if _:print()
    number=list(map(int,input().split()))
    print('Denominations:', end=' ')
    print(*number[1:])
    answer="Good coin denominations!"
    for i in range(2,len(number)):
        if number[i]<2*number[i-1]:
            answer='Bad coin denominations!'
    print(answer)
