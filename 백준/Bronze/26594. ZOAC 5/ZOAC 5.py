x=input()
now=0
count=0
while now<len(x) and x[now]==x[0]:
    now+=1
    count+=1
print(count)
