number=[int(input()) for i in range(10)]
for i in range(10):
    result=0
    for j in range(10):
        if j==i: continue
        result+=number[j]
    if result==number[i]:answer=number[i]
print(answer)
