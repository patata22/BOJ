a=list(map(int,input()))
b=list(map(int,input()))

total=-1

while a and b:
    while total!=b[-1]:
        if not a: break
        if total==-1:total=a.pop()
        else: total=(total+a.pop())%10
    if total==b[-1]:
        b.pop()
        total=-1
if sum(a)%10==0:a=[]
print('NO') if a or b else print('YES')

