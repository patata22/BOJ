record=set()
now=input()
record.add(now)
for _ in range(int(input())):
    a,b = input().split()
    if b==now:
        now=a
        record.add(now)
print(now)
print(len(record))
