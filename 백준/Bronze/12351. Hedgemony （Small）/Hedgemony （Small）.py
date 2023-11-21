for t in range(1,int(input())+1):
    n=int(input())
    number=list(map(int,input().split()))
    for i in range(1,n-1):
        number[i] = min(number[i], (number[i-1]+number[i+1])/2)
    print(f'Case #{t}: {number[-2]}')
