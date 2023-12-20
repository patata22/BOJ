input()
num=tuple(map(int,input().split()))
i=num.index(max(num))
print(sum(num[:i]))
print(sum(num[i+1:]))
     