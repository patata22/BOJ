from functools import cmp_to_key

def change(x,y):
    a=int(x+y)
    b=int(y+x)
    if a>b: return 1
    elif a<b: return -1
    else: return 0

def changeZ(x,y):
    a=int(x+zero[0]+y)
    b=int(y+zero[0]+x)
    if a>b: return -1
    elif a<b: return 1
    else: return 0
    

n=int(input())
number=input().split()
zero=[]
nero=[]

for x in number:
    if x[0]=='0': zero.append(x)
    else: nero.append(x)
if not nero:
    print('INVALID')
else:
    if zero:
        zero.sort(key=cmp_to_key(change))
        nero.sort(key=cmp_to_key(changeZ))
        first=nero.pop()
        nero.sort(key=cmp_to_key(change))
        print(first+''.join(zero)+''.join(nero))
    else:
        nero.sort(key=cmp_to_key(change))
        print(''.join(nero))
