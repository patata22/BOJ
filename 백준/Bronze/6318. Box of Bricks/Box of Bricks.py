t=0
while True:
    if t!=0:print()
    t+=1
    n=int(input())
    if n==0:break
    number=list(map(int,input().split()))
    avg=sum(number)//n
    answer=0
    for x in number:
        answer+=abs(avg-x)
    print(f'Set #{t}')
    print(f'The minimum number of moves is {answer//2}.')
