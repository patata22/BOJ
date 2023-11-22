for t in range(1,int(input())+1):
    l,n=map(int,input().split())
    l-=1
    number=list(map(lambda x: int(x)-1,input().split()))
    answer=1
    while number[l]!=-1:
        l=number[l]
        answer+=1
    print(f'Data Set {t}:\n{answer}')
    print()