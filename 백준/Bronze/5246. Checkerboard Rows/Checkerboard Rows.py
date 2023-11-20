for _ in range(int(input())):
    count=[0]*9
    number=list(map(int,input().split()))
    for i in range(2,len(number),2):
        count[number[i]]+=1
    print(max(count))
