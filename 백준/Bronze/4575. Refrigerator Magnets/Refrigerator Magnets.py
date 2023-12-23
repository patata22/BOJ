while True:
    x=input()
    if x=='END': break
    flag=True
    for i in range(65,91):
        if x.count(chr(i))>1:flag=False
    if flag:print(x)
