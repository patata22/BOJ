def sol(n,k):
    temp=0
    while n:
        temp+=n%k
        n//=k
    return temp

for i in range(1000,10000):
    if sol(i,10)==sol(i,12)==sol(i,16):print(i) 
        
        

