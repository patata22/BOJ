x=input()
answer=[]
for i in range(len(x)):
    answer.append(x[i:])
answer.sort()
print(answer.pop())