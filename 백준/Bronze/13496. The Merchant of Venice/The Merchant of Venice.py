for _ in range(int(input())):
    if _!=0:print()
    n,s,d=map(int,input().split())
    answer=0
    for __ in range(n):
        di,v=map(int,input().split())
        if s*d>=di: answer+=v
    print(f'Data Set {_+1}:')
    print(answer)