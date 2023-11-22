import sys
input=sys.stdin.readline

M,J,m,j=0,0,0,0
for _ in range(int(input())):
    a,b=input().split()
    if a=='M':
        m+=1
        M+=int(b)
    else:
        j+=1
        J+=int(b)

if not M and not J: print('V')
elif not M: print('J')
elif not J: print('M')
else:
    M*=j
    J*=m
    if M>J:print('M')
    elif M<J:print('J')
    else:print('V')
    
