while True:
    try:
        record=set()
        for _ in range(int(input())):
            x=tuple(sorted(list(set(list(input())))))
            record.add(x)
        print(len(record))
    except EOFError:break

