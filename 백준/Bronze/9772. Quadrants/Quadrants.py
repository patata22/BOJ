while True:
    a,b=map(float,input().split())
    if not a or not b: print('AXIS')
    elif a>0 and b>0: print('Q1')
    elif a<0 and b<0: print('Q3')
    elif a>0 and b<0: print('Q4')
    else: print('Q2')
    if not a and not b: break
