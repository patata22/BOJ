n=int(input())
e=0
for x in map(int,input().split()):
    if not x%2: e+=1
if 2*e>n: print('Happy')
else: print('Sad')
