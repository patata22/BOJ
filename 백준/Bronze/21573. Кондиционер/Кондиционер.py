a,b=map(int,input().split())
cmd=input()
if cmd=='auto':
    print(b)
elif cmd=='heat':
    if a<b: print(b)
    else: print(a)
elif cmd=='freeze':
    if a>b: print(b)
    else: print(a)
else: print(a)
    
