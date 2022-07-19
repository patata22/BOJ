import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)


def sol(start,cnt,score):
    global answer
    if cnt==11:
        answer=max(answer,score)
        return
    for i in range(start,11):
        if not used[i]:
            used[i]=1
            for j in range(11):
                if player[i][j] and not position[j]:
                    position[j]=1
                    sol(i+1, cnt+1,score+player[i][j])
                    position[j]=0
            used[i]=0

for _ in range(int(input())):
    player=[list(map(int,input().split())) for i in range(11)]
    used=[0]*11
    position=[0]*11
    answer=0
    sol(0,0,0)
    print(answer)

