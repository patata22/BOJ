input()
n=sorted(list(map(int,input().split())))
m=n.pop()
print(len(n)*m+sum(n))