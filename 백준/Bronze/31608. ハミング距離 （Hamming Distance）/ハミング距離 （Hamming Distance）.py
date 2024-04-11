answer=0
n=int(input())
a=input()
b=input()
for i in range(n):
    if a[i]!=b[i]:answer+=1
print(answer)