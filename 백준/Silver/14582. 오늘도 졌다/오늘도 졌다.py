gemini=list(map(int,input().split()))
start=list(map(int,input().split()))
now_g=0
now_s=0
answer='No'
for i in range(9):
    now_g+=gemini[i]
    if now_g>now_s:answer='Yes'
    now_s+=start[i]


print(answer)
