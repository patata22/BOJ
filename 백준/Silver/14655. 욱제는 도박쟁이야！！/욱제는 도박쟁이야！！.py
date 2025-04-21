input()
print(sum([sum(map(lambda x:abs(int(x)),input().split())) for i in range(2)]))