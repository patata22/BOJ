for _ in range(int(input())):
    answer='no'
    number=list(map(int,input().split()))
    size=number[0]
    for i in range(1,len(number),2):
        if number[i]+number[i+1]!=size: answer='yes'
    print(answer)
    
