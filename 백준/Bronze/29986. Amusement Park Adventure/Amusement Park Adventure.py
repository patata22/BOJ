n,h=map(int,input().split())
print(sum(map(lambda x: 1 if int(x)<=h else 0, input().split())))