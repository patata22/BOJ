n=int(input())

x=sorted(list(enumerate(list(map(int,input().split())))),key=lambda x:x[1])
print(1,end=' ')
for x,y in x:print(x+2,end=' ')
