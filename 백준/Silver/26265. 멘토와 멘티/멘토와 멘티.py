import sys
input=sys.stdin.readline

me=[]
mt={}
for _ in range(int(input())):
    a,b=input().split()
    if a not in mt:
        mt[a]=[b]
        me.append(a)
    else: mt[a].append(b)

me.sort()
for x in me:
    for y in sorted(mt[x],reverse=True):
        print(x,y)
        
