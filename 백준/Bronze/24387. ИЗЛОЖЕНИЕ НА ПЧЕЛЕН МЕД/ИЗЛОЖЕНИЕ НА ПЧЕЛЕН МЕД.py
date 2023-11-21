price=list(map(int,input().split()))
honey=list(map(int,input().split()))
price.sort()
honey.sort()
answer=[price[i]*honey[i] for i in range(3)]
print(sum(answer))