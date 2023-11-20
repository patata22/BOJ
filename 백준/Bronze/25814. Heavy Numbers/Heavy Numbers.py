def calc(x):
    x=int(x)
    l=0
    total=0
    while x:
        total+=x%10
        x//=10
        l+=1
    return l*total

a,b=map(calc,input().split())

if a>b:print(1)
elif a<b:print(2)
else:print(0)
    
