n=int(input())
head=1
for i in range(n,n-5,-1): head*=i
print(head//120)
