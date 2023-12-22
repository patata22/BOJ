def parse(c):
    return int(c[::-1])

for _ in range(int(input())):
    a,b=input().split()
    total=parse(a)+parse(b)
    print(int(str(total)[::-1]))
