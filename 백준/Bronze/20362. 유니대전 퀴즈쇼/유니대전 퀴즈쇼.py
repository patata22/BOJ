count=0
a,b = input().split()
one=b
member=[]
for _ in range(int(a)):
    a,b = input().split()
    if a==one: answer=b
    member.append((a,b))

for a,b in member:
    if a==one: break
    if b==answer: count+=1
print(count)
               
