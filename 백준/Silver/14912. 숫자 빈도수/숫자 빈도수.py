n,d=map(int,input().split())
answer=0

for i in range(1,n+1):
    while i:
        if i%10==d: answer+=1
        i//=10
print(answer)
