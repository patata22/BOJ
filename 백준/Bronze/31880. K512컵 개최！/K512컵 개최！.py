input()
answer=sum(map(int,input().split()))
for x in map(int,input().split()):
    if x:answer*=x
print(answer)
