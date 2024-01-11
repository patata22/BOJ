change={}
for i in range(ord('F'), 91):
    change[chr(i)]=chr(i-5)
change['A']='V'
change['B']='W'
change['C']='X'
change['D']='Y'
change['E']='Z'

def c(x):
    if x in change:return change[x]
    return x

while True:
    x=input()
    if x=='ENDOFINPUT':break
    if x=='START':
        while True:
            x=input()
            if x=='END':break
            print(''.join(map(c,x)))
            
            
    
