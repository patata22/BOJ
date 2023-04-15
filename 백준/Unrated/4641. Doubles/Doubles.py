while True:
    temp=input()
    if temp=='-1':break
    number=list(map(int,temp.split()))
    answer=0
    for x in number:
        if x and x*2 in number:answer+=1
    print(answer)
    
