def change(x):
    result=0
    x=int(x)
    while x>1:
        x//=2
        result+=1
    return result

def calc(x):
    a,b=divmod(count[x],x)
    if b: a+=1
    return a

n=int(input())
number=list(map(lambda x: change(x), input().split()))

count=[0]*17
for x in number:count[x]+=1

answer=0
flag=False
for i in range(16,-1,-1):
    a,b=divmod(count[i],1<<i)
    answer+=a
    if b:
        count[i-1]+=b//2
        if b%2: flag=True

print(answer+flag)