def switch(x):
    if x==1:return 0
    else:return 1
def pelin_range(x):
    left=x
    right=x
    try:
        while bulb[left]==bulb[right]:
            left-=1
            right+=1
    except IndexError:pass
    return (left+1, right-1)
n=int(input())
bulb=[2]+list(map(int,input().split()))
s=int(input())
for _ in range(s):
    a,b=map(int,input().split())
    if a==1:
        for i in range(1,n+1):
            if i%b==0:bulb[i]=switch(bulb[i])
    elif a==2:
        try:
            for i in range(pelin_range(b)[0], pelin_range(b)[1]+1):
                bulb[i]=switch(bulb[i])
        except KeyError:break
for i in range(1, n+1, 20):
    try:
        for j in range(i, i+20):
            print(bulb[j], end= ' ')
        print('')
    except IndexError:pass
