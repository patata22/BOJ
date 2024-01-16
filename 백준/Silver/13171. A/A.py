DIV=1000000007

def sol(a,b):
    if b==1: return a
    temp=sol(a,b//2)
    if b%2: return ((temp%DIV)*(temp%DIV)*a%DIV)%DIV
    else: return ((temp%DIV)*(temp%DIV))%DIV

print(sol(int(input()),int(input())))
