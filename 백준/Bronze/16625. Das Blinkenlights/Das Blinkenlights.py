def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

p,q,s=map(int,input().split())
print('yes') if p*q//gcd(p,q)<=s else print('no')