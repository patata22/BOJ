import sys
input=sys.stdin.readline

MAX=1040001


def sol():
    if water>prefix[-1]:
        print('OVERFLOW')
        return
    elif water==0:
        print('0.00')
        return
    l=0
    r=MAX+1
    while l+1<r:
        mid=(l+r)//2
        if prefix[mid]>=water: r=mid
        else: l=mid
        
    size=prefix[r]-prefix[r-1]
    left=water-prefix[r-1]
    print(f'{r-1+(left/size):.2f}')

n=int(input())

number=[tuple(map(int,input().split())) for i in range(n)]

water=int(input())

prefix=[0]*(MAX+1)
for b,h,w,d in number:
    temp=w*d
    prefix[b+1]+=temp
    prefix[b+h+1]-=temp

for i in range(1,MAX+1):
    prefix[i]+=prefix[i-1]

for i in range(1,MAX+1):
    prefix[i]+=prefix[i-1]

sol()