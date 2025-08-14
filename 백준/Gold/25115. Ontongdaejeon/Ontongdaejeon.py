def sol():
    l=0
    r=10**15
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else: l=mid
    return r

def check(now):
    point=0
    for i in range(n):
        if now+point>=reverse[i]: return True
        price=number[i]
        last=price%10
        if last<=point:
            point-=last
            price-=last
        if now<price: return False
        now-=price
        point+=price//10
    return True
        

n=int(input())

number=tuple(map(int,input().split()))

reverse=[0]*n
reverse[-1]=number[-1]
for i in range(n-2,-1,-1):
    reverse[i]=reverse[i+1]+number[i]
print(sol())