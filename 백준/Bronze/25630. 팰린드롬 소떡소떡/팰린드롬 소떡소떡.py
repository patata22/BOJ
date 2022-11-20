n=int(input())
answer=0
pal = input()
for i in range(n//2):
    if pal[i]!=pal[-i-1]:answer+=1
print(answer)
