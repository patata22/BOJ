def check(x):
    count=0
    for i in range(7):
        if x[i]=='1': count+=1
    if int(x[-1])==count%2: return 0
    return 1

for _ in range(int(input())):
    answer=0
    x=input()
    for i in range(0,len(x),8):
        answer+=check(x[i:i+8])
    print(answer)         