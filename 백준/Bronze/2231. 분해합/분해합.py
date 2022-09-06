n=int(input())
lst=[]
if n<=18:
    for i in range(1,n):
        subsum=0
        for x in str(i):
            subsum+=int(x)
        if subsum+i==n:lst.append(i)
else:
    for i in range(n-9*len(str(n)), n):
        subsum=0
        for x in str(i):
            subsum+=int(x)
        if subsum+i==n:lst.append(i)
if len(lst)==0:print(0)
else:print(lst[0])
