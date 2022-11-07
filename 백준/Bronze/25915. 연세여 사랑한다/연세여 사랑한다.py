Y = "ILOVEYONSEI"
answer=0
for i in range(1,len(Y)):
    answer+=abs(ord(Y[i])-ord(Y[i-1]))

print(abs(ord(input())-ord('I'))+answer)
