a,b=0,0
for i in range(1,10):
    print('? A',i, flush=True)
    result=int(input())
    if result==1:
        a=i
        break
for i in range(1,10):
    print('? B',i, flush=True)
    result=int(input())
    if result==1:
        b=i
        break

print('!',a+b)

        
