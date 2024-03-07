n=int(input())
a,pa,b,pb=map(int,input().split())

maximize=0
answer=[0,0]
for i in range(n//pa+1):
    power = a*i + ((n-(pa*i))//pb)*b
    if power>maximize:
        maximize=power
        answer=[i, ((n-(pa*i))//pb)]
print(*answer)
        
