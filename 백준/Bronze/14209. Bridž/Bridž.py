answer=0
for _ in range(int(input())):
    for x in input():
        if x=='A': answer+=4
        elif x=='K': answer+=3
        elif x=='Q':answer+=2
        elif x=='J':answer+=1

print(answer)
