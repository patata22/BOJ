def sol():
    l=0
    r=10**16
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else: l=mid
    if r%10: return r//10+1
    return r//10

def check(cash):
    point=0
    for price in number:
        if price>point+cash: return False
        cashUse=min(cash,price)
        pointUse=price-cashUse
        cash-=cashUse
        point-=pointUse
        point+=cashUse//10
    return True

n=int(input())
number=tuple(map(lambda x: int(x)*10,input().split()))
print(sol())
