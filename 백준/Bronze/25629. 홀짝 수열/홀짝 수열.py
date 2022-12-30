n=int(input())

odd=0
even=0
for x in map(int,input().split()):
    if x%2:odd+=1
    else: even+=1
print(int(odd in (even, even+1)))