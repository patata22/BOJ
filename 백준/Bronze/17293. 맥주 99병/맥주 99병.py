def sol(n):
    if n==0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        if N==1:
            print(f"Go to the store and buy some more, {N} bottle of beer on the wall.")
        else:
            print(f"Go to the store and buy some more, {N} bottles of beer on the wall.")
        return
    elif n==1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    elif n==2:
        print("2 bottles of beer on the wall, 2 bottles of beer.")
        print("Take one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print(f'{n} bottles of beer on the wall, {n} bottles of beer.')
        print(f'Take one down and pass it around, {n-1} bottles of beer on the wall.')
    print()
    sol(n-1)
N=int(input())
sol(N)
