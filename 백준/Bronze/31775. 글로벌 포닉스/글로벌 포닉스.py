temp=set()
for i in range(3):
    x=input()
    if x[0] in 'lkp':temp.add(x[0])
print('GLOBAL') if len(temp)==3 else print('PONIX')
