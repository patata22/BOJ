n=int(input())
answer=0
for x in map(int,input().split()):answer+=min(x,n)
print(answer)