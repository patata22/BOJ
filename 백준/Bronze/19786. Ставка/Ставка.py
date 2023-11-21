import sys
input=sys.stdin.readline

def calc(r,g,b):
    return a*(r**2+g**2+b**2)+c*min(r,g,b)

for _ in range(int(input())):
    a,c=map(int,input().split())
    r,g,b=map(int,input().split())
    answer=0
    money=0
    r+=1
    if calc(r,g,b)>money:
        answer='RED'
        money=calc(r,g,b)
    r-=1
    g+=1
    
    if calc(r,g,b)>money:
        answer='GREEN'
        money=calc(r,g,b)
    g-=1
    b+=1
    if calc(r,g,b)>money:
        answer='BLUE'
    print(answer)