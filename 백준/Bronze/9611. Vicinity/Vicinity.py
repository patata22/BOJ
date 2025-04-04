def calc(x,y,d):
    result=0
    for a,b in point:
        if (x-a)**2+(y-b)**2<=d:
            result+=1
    return result-1
        

n=int(input())
point=[tuple(map(int,input().split())) for i in range(n)]

for tt in range(int(input())):
    a,b=map(int,input().split())
    print(calc(*point[a-1],b**2))
    
      
