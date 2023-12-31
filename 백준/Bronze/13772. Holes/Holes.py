def parse(x):
    if x in 'ADOPQR': return 1
    if x=='B':return 2
    return 0

for _ in range(int(input())):
    print(sum(map(parse,input())))