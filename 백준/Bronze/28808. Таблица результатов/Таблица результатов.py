a,b=map(int,input().split())
answer=0
for _ in range(a):
    if '+' in input(): answer+=1
print(answer)
