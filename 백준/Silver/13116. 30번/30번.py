import sys
input=sys.stdin.readline

def sol(a,b):
    n1=[]
    n2=[]
    while a:
        n1.append(a)
        a//=2
    while b:
        n2.append(b)
        b//=2
    n1.sort(reverse=True)
    n2.sort(reverse=True)
    for x in n1:
        for y in n2:
            if x==y:return 10*x

for _ in range(int(input())):
    print(sol(*map(int,input().split())))
        
