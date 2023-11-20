pi=3.1415926535897932384626

for t in range(int(input())):
    if t: print()
    b,w=input().split()
    w=float(w)
    total=0
    for _ in range(int(b)):
        total+=4*pi*(float(input())**3)/3000
    print(f'Data Set {t+1}:' )
    print('Yes') if total>w else print('No')
