n,c=map(int,input().split())

total=0
bed=0
bal=0
for _ in range(n):
    a,b=input().split()
    if b=="bedroom": bed+=int(a)
    elif b=='balcony': bal+=int(a)
    total+=int(a)

print(total)
print(bed)
print((total-0.5*bal)*c)
