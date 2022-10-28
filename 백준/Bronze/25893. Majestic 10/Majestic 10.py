record={0:"zilch", 1: "double", 2:"double-double", 3:"triple-double"}

for _ in range(int(input())):
    if _!=0: print()
    temp=tuple(map(int,input().split()))
    answer=0
    for x in temp:
        if x>=10: answer+=1
    print(*temp)
    print(record[answer])
    
