name=[input() for i in range(int(input()))]

for x in name:
    print('?',x, flush=True)
    result=int(input())
    print('?',x, flush=True)
    result+=int(input())
    if result:
        print('!',x)
        break
