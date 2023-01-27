temp = float('inf')
answer=""
while True:
    try:
        a,b=input().split()
        if int(b)<temp:
            temp=int(b)
            answer=a
    except EOFError:
        print(answer)
        break