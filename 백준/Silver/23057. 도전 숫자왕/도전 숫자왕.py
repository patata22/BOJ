able=set()

def choice(i):
    global now
    if i==n:
        able.add(now)
        return
    choice(i+1)
    now += number[i]
    choice(i+1)
    now -= number[i]
    
n=int(input())
number=list(map(int,input().split()))
total = sum(number)
used=[0]*n
now=0
choice(0)

print(total+1-len(able))