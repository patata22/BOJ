temp=[]
for _ in range(int(input())):
    x,y,v=map(int,input().split())
    t= ((x**2)+(y**2))/v**2
    temp.append((t,_+1))
temp.sort()
for _,i in temp:
    print(i)
