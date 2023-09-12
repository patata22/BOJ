def sol(x):
    if x>4500: return "Round 1"
    elif x>1000: return "Round 2"
    elif x>25: return 'Round 3'
    return "World Finals"

for _ in range(int(input())):
    print(f'Case #{_+1}: {sol(int(input()))}')
    
