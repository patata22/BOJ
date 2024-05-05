n,a=map(int,input().split())
number=list(map(int,input().split()))
answer=0
for x in number:
    answer+=x//a
print(answer)
