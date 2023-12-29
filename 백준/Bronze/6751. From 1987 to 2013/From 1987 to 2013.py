n=int(input())
while True:
    n+=1
    temp=set()
    x=n
    while x:
        temp.add(x%10)
        x//=10
    if len(temp)==len(str(n)): break
print(n)
