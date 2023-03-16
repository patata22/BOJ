def solution(numer1, denom1, numer2, denom2):
    head = numer1*denom2+numer2*denom1
    tail = denom1*denom2
    g=gcd(head,tail)
    head//=g
    tail//=g
    
    return head,tail

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x