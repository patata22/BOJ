n=int(input())
answer=sum(map(lambda x: float(x)**3, input().split()))
print(answer**(1/3))