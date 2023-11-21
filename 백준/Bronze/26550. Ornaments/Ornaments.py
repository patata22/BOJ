answer=[ i*(i+1)//2 for i in range(1000001)]
for i in range(1,1000001): answer[i]+=answer[i-1]
for _ in range(int(input())):
    print(answer[int(input())])
    