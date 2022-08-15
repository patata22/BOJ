a=input()
b=input()
z=""
x=""
c=""
v=""
n=""
for i in range(100000):
    A=int(a[i])
    B=int(b[i])
    z+=str(A&B)
    x+=str(A|B)
    c+=str(A^B)
    v+=str(1-A)
    n+=str(1-B)

print(z,x,c,v,n, sep="\n")
