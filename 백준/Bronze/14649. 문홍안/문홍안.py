p=int(input())
n=int(input())

number=[0]*100
for _ in range(n):
    a,b=input().split()
    a=int(a)
    if b=='R':
        for i in range(a,100):
            number[i]+=1
    else:
        for i in range(a-2,-1,-1):
            number[i]+=1
for i in range(100):
    number[i]%=3
for i in range(3):
    print(f'{p*number.count(i)/100:.2f}')
