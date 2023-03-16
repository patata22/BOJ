def solution(a, b):
    g=gcd(a,b)
    b//=g
    while not b%2:
        b//=2
    while not b%5:
        b//=5
    if b==1:return 1
    else: return 2

def gcd(x,y):
    while y: x,y=y,x%y
    return x