t=0
s=0
for _ in range(int(input())):
    temp=input()
    t+=temp.count('t')+temp.count('T')
    s+=temp.count('s')+temp.count('S')

if t<=s: print('French')
else:print('English')
