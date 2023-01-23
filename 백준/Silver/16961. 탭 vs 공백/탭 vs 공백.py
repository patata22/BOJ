TAB = [0]*367
SPACE = [0]*367

total=0
most=0
nofight=0
nofightmost=0
longest=0

for _ in range(int(input())):
    a,s,e=input().split()
    s,e=int(s),int(e)
    if a=='T':
        for i in range(s,e+1):
            TAB[i]+=1
    else:
        for i in range(s,e+1):
            SPACE[i]+=1
    longest=max(longest, e-s+1)

for i in range(1,367):
    temp=TAB[i]+SPACE[i]
    if temp:total+=1
    most = max(most, temp)
    if TAB[i]==SPACE[i] and TAB[i] and SPACE[i]:
        nofight+=1
        nofightmost = max(nofightmost,temp)

print(total)
print(most)
print(nofight)
print(nofightmost)
print(longest)
       