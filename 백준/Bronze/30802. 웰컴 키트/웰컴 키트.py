n=int(input())
answer=0
number=list(map(int,input().split()))
t,p=map(int,input().split())
for x in number:
    answer+=x//t
    if x%t: answer+=1
print(answer)
print(*divmod(n,p))
