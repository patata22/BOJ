for _ in range(int(input())):
    log= input()
    front=[]
    back=[]
    for key in log:
        if key=='<':
            if front: back.append(front.pop())
        elif key=='>':
            if back: front.append(back.pop())
        elif key=='-':
            if front: front.pop()
        else: front.append(key)
    print(''.join(front)+''.join(back[::-1]))