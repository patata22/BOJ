import sys
input=sys.stdin.readline

time=[]
for _ in range(int(input())):
    time.append(sum(list(map(int,input().split()))[1:]))
time.sort(reverse=True)
answer=0
while time:
    l=len(time)
    answer+=l*time.pop()
print(answer)
