import sys
input=sys.stdin.readline

def check(x):
    return a>=q*x and b>=w*x and c>=e*x and d>=r*x
    

a,b,c,d=map(int,input().split())
q,w,e,r=map(int,input().split())

cookie=0

for _ in range(int(input())):
    x,y=map(int,input().split())
    if x==1:
        if check(y):
            cookie+=y
            a-=q*y
            b-=w*y
            c-=e*y
            d-=r*y
            print(cookie)
        else: print('Hello, siumii')
    elif x==2:
        a+=y
        print(a)
    elif x==3:
        b+=y
        print(b)
    elif x==4:
        c+=y
        print(c)
    elif x==5:
        d+=y
        print(d)
