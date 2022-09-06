def prime(x):
    answer=0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:answer=1
    if answer==0:return True
    else:return False
    
count=0
n=int(input())
lst=list(map(int,input().split()))
if 1 in lst:lst.remove(1)
for x in lst:
    if prime(x) is True:count+=1
print(count)