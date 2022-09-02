for _ in range(int(input())):
    answer=0
    for x in input():
        if x=='U':answer+=1
        else:
            break
    print(answer)
