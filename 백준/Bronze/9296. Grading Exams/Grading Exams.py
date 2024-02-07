for _ in range(1,int(input())+1):
    n=int(input())
    x=input()
    y=input()
    answer=0
    for i in range(n):
        if x[i]!=y[i]:answer+=1
    print(f'Case {_}: {answer}')
