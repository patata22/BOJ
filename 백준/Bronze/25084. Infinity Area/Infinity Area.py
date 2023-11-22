pi=3.14159265358979

for _ in range(int(input())):
    r,a,b=map(int,input().split())
    answer=r*r*pi
    while r>=1:
        r*=a
        answer+=r*r*pi
        r//=b
        if r<1: break
        answer+=r*r*pi
    print(f'Case #{_+1}: {answer}')
        
