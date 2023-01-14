for _ in range(int(input())):
    a,b,c= input().split()
    for i in range(len(a)):
        if i in range(int(b),int(c)):continue
        print(a[i],end='')
    print()
    
