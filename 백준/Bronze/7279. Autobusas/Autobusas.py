n,k=map(int,input().split())
seat=0
answer=0
for _ in range(n):
    a,b=map(int,input().split())
    seat+=a-b
    if seat>k: answer=max(answer,seat-k)
print(answer)
