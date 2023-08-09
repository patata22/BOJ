pi=3.14159

def cone(x,y):
    return 1/3*cylinder(x,y)

def cylinder(x,y):
    return pi*(x*x)*y

def sphere(x):
    return (4/3)*pi*(x**3)
answer=0
for _ in range(int(input())):
    temp=input().split()
    if temp[0]=='S': answer=max(answer,sphere(float(temp[1])))
    elif temp[0]=='C': answer = max(answer,cylinder(float(temp[1]),float(temp[2])))
    else: answer = answer=max(answer,cone(float(temp[1]), float(temp[2])))
print("%.3f" %answer)
    
