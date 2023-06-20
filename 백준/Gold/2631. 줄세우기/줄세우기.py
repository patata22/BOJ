n=int(input())
number=[int(input()) for i in range(n)]
count=[1]*n
for i in range(n):
    for j in range(i):
        if number[i]>number[j]:
            count[i]=max(count[i], count[j]+1)
print(n-max(count))
