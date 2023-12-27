def check(x):
    x=list(map(int,str(x)))
    for i in range(1,len(x)):
        if x[i]<x[i-1]: return False
    return True
    

for _ in range(int(input())):
    x=int(input())
    while not check(x):
        x-=1
    print(f'Case #{_+1}: {x}')
    
    
