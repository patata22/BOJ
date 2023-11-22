n=int(input())
total=0
x=0
while n>=total+(x+1)**2:
    x+=1
    total+=x**2
print(x)