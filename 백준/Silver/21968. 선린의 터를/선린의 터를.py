
for _ in range(int(input())):
    n=int(input())
    answer=0
    num=list(bin(n)[2:])
    mul=1
    while num:
        temp=num.pop()
        if temp=='1':
            answer+=mul
        mul*=3
    print(answer)
