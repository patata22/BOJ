n=int(input())
answer=0
a=tuple(map(int,input().split()))
b=tuple(map(int,input().split()))
for i in range(n):
    answer+=abs(a[i]-b[i])
print(answer//2)
