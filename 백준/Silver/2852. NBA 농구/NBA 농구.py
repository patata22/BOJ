def change(x):
    m=x//60
    s=x%60
    if m<10: m='0'+str(m)
    else: m=str(m)
    if s<10: s='0'+str(s)
    else: s=str(s)
    return m+':'+s

one=[0]*2881
two=[0]*2881

for _ in range(int(input())):
    a,b=input().split()
    m,s=map(int,b.split(':'))
    if a=='1':one[60*m+s]+=1
    else: two[60*m+s]+=1

for i in range(1,2881):
    one[i]+=one[i-1]
    two[i]+=two[i-1]

a=0
b=0
for i in range(2880):
    if one[i]>two[i]: a+=1
    elif one[i]<two[i]: b+=1

print(change(a))
print(change(b))
