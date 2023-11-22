r,f=map(int,input().split())
degree=(180*f/r)%360
if 0<=degree<90 or 270<=degree:print('up')
else:print('down')