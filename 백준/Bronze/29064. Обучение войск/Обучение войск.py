n=int(input())
one=input().split().count('1')
print(max(0,(n+1)//2-one))
