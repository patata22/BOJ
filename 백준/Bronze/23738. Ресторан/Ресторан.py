change={}
for x in 'AKMOT': change[x]=x.lower()
change['B']='v'
change['E']='ye'
change['H']='n'
change['P']='r'
change['C']='s'
change['Y']='u'
change['X']='h'

for x in input():
    print(change[x],end='')
