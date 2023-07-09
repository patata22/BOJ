answer=0
x=input()
while True:
    try:
        answer+=input().count(x)
    except EOFError:
        print(answer)
        break
