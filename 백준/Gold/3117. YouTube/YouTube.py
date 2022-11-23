n,k,m = map(int,input().split())
m-=1
MAX = 30

table =  [[0]*MAX for i in range(k+1)]
student= tuple(map(int,input().split()))
recommend= tuple(map(int,input().split()))
for i in range(1,k+1):
    table[i][0] = recommend[i-1]
    
for j in range(1,MAX):
    for i in range(1,k+1):
        table[i][j] = table[table[i][j-1]][j-1]

temp = []
for i in range(MAX):
    if (m-1)>>i&1: temp.append(i)


answer= []
for x in student:
    now = recommend[x-1]
    for y in temp:
        now = table[now][y]
    answer.append(now)
print(*answer)

