for _ in range(int(input())):
    a,b=map(int,input().split())
    answer=round((a*b)/(a+b),1)
    print(f'f = {answer}')
