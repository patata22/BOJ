p,a=map(int,input().split())
acc= sorted(list(map(int,input().split())), reverse=True)
answer=0
while p<200 and acc:
    p+=acc.pop()
    answer+=1
print(answer)
