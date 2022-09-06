input()
time=list(map(int,input().split()))
time.sort(reverse=True)
answer=0
while time:
    answer+=time.pop()*(len(time)+1)
print(answer)
