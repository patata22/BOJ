for _ in range(int(input())):
    answer=0
    for _ in range(int(input())):
        a,b,c=input().split()
        answer+=int(b)*float(c)
    print(f'${round(answer,2):.2f}')