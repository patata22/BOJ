import math

def sol():
    w,h=map(int,input().split())
    n,a,b=map(int,input().split())
    count=(w//a)*(h//b)  
    if not count: return -1     
    else: return math.ceil(n/count)
        
print(sol())