def binary_search(i):
    a = A[i]
    l=i-1
    r=n
    while l+1<r:
        mid = (l+r)//2
        if B[mid]>a:r=mid
        else:l=mid
    return l-i
n=int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

answer=[]
for i in range(n): answer.append(binary_search(i))
print(*answer)
