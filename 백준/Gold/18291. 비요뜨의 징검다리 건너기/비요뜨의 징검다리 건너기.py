DIV=10**9+7

def calc(x):
    if x==1: return 2
    temp=calc(x//2)
    if x%2:
        return ((temp%DIV)*(temp%DIV)*2)%DIV
    else:
        return (temp%DIV)*(temp%DIV)%DIV


for _ in range(int(input())):
    n=int(input())
    if n<=2: print(1)
    else:
        print(calc(n-2))
