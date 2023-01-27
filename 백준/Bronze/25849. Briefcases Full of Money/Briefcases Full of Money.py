dollar = (1,5,10,20,50,100)
total = list(map(int,input().split()))
for i in range(6):
    total[i]*=dollar[i]
print(dollar[sorted(list(enumerate(total)),key=lambda x: x[1])[-1][0]])
