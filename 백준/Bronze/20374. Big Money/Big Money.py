from decimal import *
import sys
input=sys.stdin.readline
answer=Decimal(0)
while True:
    try:answer+=Decimal(input().rstrip())
    except:break
print('%.2f' %float(answer))
