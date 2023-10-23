n,m=map(int,input().split())

number=list(map(lambda x: int(x)%m,input().split()))

print(1-bool(sum(number)%m))
