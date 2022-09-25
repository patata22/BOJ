n=int(input())
word=list(input())
answer_b=1
answer_r=1
now_b='B'
now_r='R'
for i in range(n):
    if word[i]=='B':
        if now_b=='R':
            now_b='B'
        if now_r=='R':
            answer_r+=1
            now_r='B'
    else:
        if now_b=='B':
            answer_b+=1
            now_b='R'
        if now_r=='B':
            now_r='R'
            
print(min(answer_b, answer_r))