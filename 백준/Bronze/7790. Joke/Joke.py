answer=0
while True:
    try:
        answer+=input().count('joke')
    except EOFError:
        print(answer)
        break