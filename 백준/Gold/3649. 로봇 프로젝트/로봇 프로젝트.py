import sys
input=sys.stdin.readline

def sol():
    for i in range(n):
        now=number[i]
        gap=X-now
        l=i
        r=n+1
        while l+1<r:
            mid=(l+r)//2
            if number[mid]==gap: return f'yes {now} {number[mid]}'
            elif number[mid]<gap: l=mid
            else: r=mid
    return 'danger'
    

while True:
    try:
        X=int(input())*10**7
        n=int(input())
        number=sorted([int(input()) for i in range(n)])
        number.append(float('inf'))
        print(sol())
    except:break
