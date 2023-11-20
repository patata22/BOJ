n=int(input())
x=[0,min(209,n+8)-n,min(219,n+4)-n,min(229,n+2)-n,1]
print(x.index(max(x)))