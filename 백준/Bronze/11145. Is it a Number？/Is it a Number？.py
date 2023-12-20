for _ in range(int(input())):
    try:
        x=int(input())
        if x<0: raise Exception
        print(x)
    except:
        print('invalid input')
