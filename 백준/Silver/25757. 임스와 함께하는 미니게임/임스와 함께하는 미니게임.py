import sys
input=sys.stdin.readline

n,g=input().rstrip().split()
n=int(n)
name=set()
for _ in range(n):
    name.add(input().rstrip())

if g=='Y': print(len(name))
elif g=='F': print(len(name)//2)
else: print(len(name)//3)
    

