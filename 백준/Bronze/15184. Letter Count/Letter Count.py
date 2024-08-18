temp=input().upper()
count=[0]*26
for i in range(65,91):
    x=temp.count(chr(i))
    count[i-65]+=x

for i in range(65,91):
    print(f'{chr(i)} | {"*"*count[i-65]}')
