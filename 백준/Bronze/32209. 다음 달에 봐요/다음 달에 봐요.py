def sol():
    problem=0
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if a==1: problem+=b
        else:
            if problem<b: return 'Adios'
            problem-=b
    return 'See you next month'
               
print(sol())