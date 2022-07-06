def total(x):
    answer=0
    for tree in trees:
        if tree>x:answer+=tree-x
    if answer>=m:return True
    else:return False
    
def binary_search():
    st,en=0,max(trees)
    while st<en:
        mid=(st+en+1)//2
        if total(mid):st=mid
        else:en=mid-1
    return st


n,m=map(int,input().split())
trees=list(map(int,input().split()))
print(binary_search())
