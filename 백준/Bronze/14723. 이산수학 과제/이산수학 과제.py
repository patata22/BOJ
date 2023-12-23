n=int(input())
now=1
while n-now>0:
    n-=now
    now+=1
head=now
tail=1
for i in range(n-1):
    head-=1
    tail+=1
print(head,tail)

