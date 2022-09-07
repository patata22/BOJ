import sys
input=sys.stdin.readline

total=0
xor=0
for _ in range(int(input())):
    x=input().rstrip()
    if len(x.split())>1:
        a,b=map(int,x.split())
        if a==1:
            total+=b
            xor^=b
        elif a==2:
            total-=b
            xor^=b
    else:
        print(total) if x=='3' else print(xor)
   