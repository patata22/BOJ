n=int(input())
x,s=map(int,input().split())
answer='NO'
for _ in range(n):
    c,p=map(int,input().split())
    if c<=x and p>s: answer='YES'
print(answer)
