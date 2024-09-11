import sys
input=sys.stdin.readline

for tt in range(int(input())):
    r,c=map(int,input().split())
    if r!=c:
        print('jinseo')
        print(min(r,c),min(r,c))
    else:print('dohoon')