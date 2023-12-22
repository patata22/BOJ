answer=[0]*68
answer[0]=1
answer[1]=1
answer[2]=2
answer[3]=4
for i in range(4,68):
    answer[i]=answer[i-1]+answer[i-2]+answer[i-3]+answer[i-4]

for _ in range(int(input())):
    print(answer[int(input())])
