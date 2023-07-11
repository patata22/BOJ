answer=0
for _ in range(4):
    a,b=input().split()
    if a=='Es': answer+=21*int(b)
    else: answer+=17*int(b)
print(answer)
