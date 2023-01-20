n=int(input())
a=input()
b=input()
answer=0
for i in range(n):
    if a[i]!=b[i]:answer+=1
print(answer)
