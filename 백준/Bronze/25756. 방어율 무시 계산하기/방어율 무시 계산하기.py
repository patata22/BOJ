v=0
input()
number=list(map(lambda x: int(x)/100,input().split()))
for a in number:
    v=1-(1-v)*(1-a)
    print(100*v)
