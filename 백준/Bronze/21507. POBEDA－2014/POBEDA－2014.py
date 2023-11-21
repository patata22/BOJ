from decimal import *
a,b,c,d=map(int,input().split())
print(int(Decimal.sqrt(Decimal(min(a,b)+min(c,d)))))