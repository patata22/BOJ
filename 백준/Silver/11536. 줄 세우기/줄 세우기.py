name=[input() for i in range(int(input()))]
i=sorted(name)
d=i[::-1]
if name==i: print('INCREASING')
elif name==d: print('DECREASING')
else: print('NEITHER')
