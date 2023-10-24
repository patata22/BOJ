def calc():
    for i in range(1,1000):
        for j in range(1,1000):
            total=0
            n= i*j
            while n:
                total+=n%10
                n//=10
            record.append((i,j,total))

n=map(int,input().split())
count=[0]*1001
number=list(map(int,input().split()))
for i in number:
    count[i]+=1
number=set(number)
record=[]
calc()
record.sort(key=lambda x: x[2])
while record:
    x,y,z=record.pop()
    if x in number and y in number:
        if x==y and count[x]<2: continue
        print(z)
        break