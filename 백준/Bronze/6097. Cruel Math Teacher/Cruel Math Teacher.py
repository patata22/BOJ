a,b=map(int,input().split())
x=str(a**b)
for i in range(0,len(x),70):
    print(x[i:i+70])
