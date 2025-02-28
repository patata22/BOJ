def check(x):
    total=0
    for i in range(1,x):
        if x%i==0: total+=i
    if total>x: return 1
    else: return 0

def sol(x):
    if not result[x]: return 'BOJ 2022'
    for i in range(1,x):
        if x%i: continue
        if result[i]: return 'BOJ 2022'
    return 'Good Bye'
    
result=[0]
for i in range(1,5001): result.append(check(i))
for _ in range(int(input())):
    print(sol(int(input())))