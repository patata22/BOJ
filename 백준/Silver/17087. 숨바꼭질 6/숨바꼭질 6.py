def gcd(x,y):
    while y: x,y=y,x%y
    return x

n,s=map(int,input().split())
place=list(map(lambda x: abs(int(x)-s), input().split()))
answer=place[0]
for i in range(1,n):
    answer=gcd(answer,place[i])
print(answer)



        
