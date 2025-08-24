def solve():
    n, a, b = map(int, input().split())
    s, t = map(int, input().split())

    if a < s < b and a < t < b:
        print("City")
        return
    if (s <= a and t <= a) or (s >= b and t >= b):
        print("Outside")
        return

    print("Full")

solve()
