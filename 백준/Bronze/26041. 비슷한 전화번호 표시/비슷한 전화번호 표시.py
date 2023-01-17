answer=0
number=tuple(input().split())
target=input()
n=len(target)
for x in number:
    if len(x)<=n:continue
    elif x[:n]==target:answer+=1
print(answer)
    
