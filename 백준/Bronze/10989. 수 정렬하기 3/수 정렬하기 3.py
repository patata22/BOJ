import sys
input=sys.stdin.readline
cnt=[0]*10001
for _ in range(int(input())):
    cnt[int(input())]+=1

for i in range(1,10001):
    if cnt[i]:
        for j in range(cnt[i]):print(i) 
