def solution(arr):
    now=arr[0]
    for i in range(1,len(arr)):
        now=lcm(now,arr[i])
    return now

def gcd(x,y):
    while y: x,y=y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)