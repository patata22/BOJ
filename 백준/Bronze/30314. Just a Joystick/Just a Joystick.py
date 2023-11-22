def change(a,b):
    a=ord(a)-65
    b=ord(b)-65
    return min(abs(b-a), 26-abs(b-a))

n=int(input())
a=input()
b=input()
answer=0
for i in range(n):
    answer+=change(a[i],b[i])
print(answer)

