def binary_search(left,right):
    l=0
    r=250001
    while l+1<r:
        mid=(l+r)//2
        if left>right<<mid: l=mid
        else: r=mid
    return r


n=int(input())
number=list(map(int,input().split()))
answer=0
for i in range(1,n):
    if number[i-1]>number[i]:
        need = binary_search(number[i-1],number[i])
        number[i]<<=need
        answer+=need

print(answer)