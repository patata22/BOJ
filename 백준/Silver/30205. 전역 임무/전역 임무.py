def sol(b):
    global p
    item=0
    temp=[]
    for x in b:
        if x==-1: item+=1
        else: temp.append(x)
    for x in temp:
        if p>=x: p+=x
        else:
            while item and p<x:
                item-=1
                p*=2
            if p<x: return 0
            else: p+=x
    for i in range(item):p*=2
    return 1
    
n,m,p=map(int,input().split())
base=[sorted(list(map(int,input().split()))) for i in range(n)]

answer=1
for b in base:
    answer&=sol(b)
print(answer)
