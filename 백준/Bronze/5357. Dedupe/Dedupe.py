for _ in range(int(input())):
    answer="?"
    for x in input():
        if answer[-1]!=x:answer+=x
    print(answer[1:])
