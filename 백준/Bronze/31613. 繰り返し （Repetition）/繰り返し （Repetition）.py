x,n=int(input()),int(input())
answer=0
while x<n:
    r=x%3
    if r==0:x+=1
    else: x*=(r+1)
    answer+=1
print(answer)

