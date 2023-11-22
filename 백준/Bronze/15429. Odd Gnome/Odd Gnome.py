for _ in range(int(input())):
    number=list(map(int,input().split()))
    for i in range(2,number[0]):
        if number[i]-number[i-1]!=1:
            print(i)
            break
