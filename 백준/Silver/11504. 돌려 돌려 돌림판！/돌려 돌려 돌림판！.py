

for tt in range(int(input())):
    n,m=map(int,input().split())
    x=int(''.join(input().split()))
    y=int(''.join(input().split()))
    number=input().split()
    answer=0
    for _ in range(n):
        temp=[]
        for __ in range(m):
            temp.append(number[(_+__)%n])
        if x<=int(''.join(temp))<=y: answer+=1

    print(answer)
