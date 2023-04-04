a=int(input())
b=int(input())
c=b

print(a)
print(b)
while c:
    print(a*(c%10))
    c//=10
print(a*b)
