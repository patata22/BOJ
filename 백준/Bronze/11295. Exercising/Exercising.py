T=0
while True:
    T+=1
    n=int(input())
    if not n: break
    print(f'User {T}')
    for _ in range(int(input())):
        total=n*int(input())
        total/=100000
        print('%.5f' %total)
    
