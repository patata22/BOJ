def sol():
    budget=int(input())
    price=[int(input()) for i in range(3)]
    word=['Watermelon', 'Pomegranates', 'Nuts']
    for i in range(3):
        if price[i]<=budget: return word[i]
    return 'Nothing'
print(sol())