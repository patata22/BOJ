def gcd(x,y):
    while y:x,y=y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

while True:
    head, tail = map(int,input().split())
    if not head: break
    answer=[]
    while head:
        tt=tail//head
        if not tail%head:
            answer.append(tail)
            break
        while True:
            tt+=1
            H=head*tt-tail
            T=tail*tt
            g=gcd(H,T)
            if T//g>=1000000: continue
            head=H//g
            tail=T//g
            answer.append(tt)
            break
            
    print(*answer)
