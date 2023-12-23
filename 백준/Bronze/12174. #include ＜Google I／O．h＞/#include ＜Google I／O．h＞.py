def parse(x):
    if x=='O':return '0'
    return '1'

for __ in range(int(input())):
    n=int(input())
    temp=list(map(parse,input()))
    print(f'Case #{__+1}:',end=' ')
    for _ in range(0,8*n,8):
        print(chr(int(''.join(temp[_:_+8]),2)),end='')
    print()
        
