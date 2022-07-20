answer=0
for _ in range(int(input())):
    x=input()
    temp=x.count("for")+x.count("while")
    answer=max(answer,temp)
print(answer)
