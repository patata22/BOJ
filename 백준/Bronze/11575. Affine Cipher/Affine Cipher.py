def parse(c):
    return chr(((ord(c)-65)*a+b)%26+65)

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(''.join(map(parse, input())))