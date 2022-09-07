input()
number=list(map(int,input().split()))
for x in number:
    print(1,end=' ') if int(x**0.5)**2==x else print(0,end=' ')
