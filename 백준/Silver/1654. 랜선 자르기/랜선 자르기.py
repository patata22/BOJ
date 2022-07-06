def line_count(t):
    answer=0
    for x in number:answer+=x//t
    if answer>=n:return True
    else:return False

def binary_search():
    st,en=0,max(number)
    while st<en:
        mid=(st+en+1)//2
        if line_count(mid):st=mid
        else: en=mid-1
    return st
k,n=map(int,input().split())
number=[int(input()) for i in range(k)]
print(binary_search())
