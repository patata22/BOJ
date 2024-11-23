monitor = []
for i in range(int(input())):
    a,b=map(int,input().split())
    monitor.append((a*a+b*b,i+1))
monitor.sort(key= lambda x: (-x[0],x[1]))

for x,y in monitor:
    print(y)