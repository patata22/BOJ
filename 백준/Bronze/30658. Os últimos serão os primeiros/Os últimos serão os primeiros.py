while True:
    n=int(input())
    if not n: break
    print(*[int(input()) for i in range(n)][::-1],sep='\n')
    print(0)