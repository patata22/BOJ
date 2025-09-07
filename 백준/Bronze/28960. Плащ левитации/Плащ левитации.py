h,l,a,b=map(int,input().split())
if (l>=a and b<=2*h) or (l>=b and a<=2*h): print('YES')
else: print('NO')