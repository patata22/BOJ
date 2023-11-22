a,b,c=map(int,input().split())
mid=(a+b)//2
if a-mid==mid-b and a-mid>=c: print('YES')
else:print('NO')
