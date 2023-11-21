n,a,k=map(int,input().split())
answer=0
n-=a
while n>0:
    if n%k==0: answer=1
    n-=a
print(answer)