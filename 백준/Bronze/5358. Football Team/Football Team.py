def change(x):
    temp=list(x)
    for i in range(len(x)):
        if temp[i]=='i': temp[i]='e'
        elif temp[i]=='e':temp[i]='i'
        elif temp[i]=='I': temp[i]='E'
        elif temp[i]=='E': temp[i]='I'
    return ''.join(temp)

while True:
    try:
        print(change(input()))
    except:
        break
