na, nb=map(int,input().split())
set1=set(map(int,input().split()))
set2=set(map(int,input().split()))
lst1=list(set1-set2)
lst1.sort()
if len(lst1)==0:print(0)
else:
    print(len(lst1))
    for x in lst1:
        print(x, end=' ')