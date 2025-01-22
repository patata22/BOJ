def location(depth):
   if depth==d:
      return 0,0
   x,y=location(depth+1)
   now=number[depth]
   if now==1:
      y+=1<<(d-depth-1)
   elif now==3:
      x+=1<<(d-depth-1)
   elif now==4:
      x+=1<<(d-depth-1)
      y+=1<<(d-depth-1)
   return x,y
   
def reverse(depth,x,y):
   if depth==d:
      return
   size=1<<(d-depth-1)
   if x<size and y<size:
      answer.append('2')
      reverse(depth+1,x,y)
   elif x<size and y>=size:
      answer.append('1')
      reverse(depth+1,x,y-size)
   elif x>=size and y<size:
      answer.append('3')
      reverse(depth+1,x-size,y)
   elif x>=size and y>=size:
      answer.append('4')
      reverse(depth+1,x-size,y-size)

def sol():
   x,y=location(0)
   a,b=map(int,input().split())
   x-=b
   y+=a
   if not 0<=x<1<<d or not 0<=y<1<<d:
      answer.append('-1')
      return
   reverse(0,x,y)

d,number=input().split()
d=int(d)
number=list(map(int,number))
answer=[]
sol()
print(''.join(answer))