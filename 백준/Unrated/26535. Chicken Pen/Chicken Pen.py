now=1
n=int(input())
while now**2<n:
    now+=1

print('x'*(now+2))
for i in range(now):
    print('x'+'.'*now+'x')
print('x'*(now+2))
