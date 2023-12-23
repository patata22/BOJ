def ability(x):
    if x>=250: return 5
    elif x>=200: return 4
    elif x>=140: return 3
    elif x>=100: return 2
    elif x>=60: return 1
    else: return 0
n=int(input())
level=[int(input()) for i in range(n)]
level.sort(reverse=True)
tl=0
ta=0
for i in range(min(42,n)):
    tl+=level[i]
    ta+=ability(level[i])
print(tl,ta)

