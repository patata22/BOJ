total=0
answer=0
for _ in range(int(input())):
    total+=int(input())
    answer=max(total,answer)
print(100+answer)
