def sol():
    n=len(x)
    for i in range(1,n):
        temp=set()
        for j in range(n-i):
            temp.add(x[j]+x[j+i])
        if len(temp)!=n-i:
            
            return "NOT "
    return ""

while True:
    x=input()
    if x=='*': break
    print(f'{x} is {sol()}surprising.')
    
