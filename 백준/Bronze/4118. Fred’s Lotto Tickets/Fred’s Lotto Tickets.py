while True:
    n=int(input())
    if not n: break
    total=[0]*50
    for _ in range(n):
        for x in map(int,input().split()):
            total[x]=1
    print('Yes') if sum(total)==49 else print('No')
        
