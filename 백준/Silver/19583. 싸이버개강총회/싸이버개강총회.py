import sys
input=sys.stdin.readline

def change(x):
    h,m=x.split(':')
    return 60*int(h)+int(m)

s,e,q=map(change,input().rstrip().split())
op=set()
cl=set()
while True:
    try:
        time,name = input().rstrip().split()
        time=change(time)
        if time<=s: op.add(name)
        if e<=time<=q: cl.add(name)

    except:
        break

print(len(op&cl))