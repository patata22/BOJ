lst=[0 for i in range(11)]
lst[0]=1
lst[1]=2
lst[2]=4
for i in range(3,11):
    lst[i]=lst[i-1]+lst[i-2]+lst[i-3]
n=int(input())
for _ in range(n):
    x=int(input())
    print(lst[x-1])