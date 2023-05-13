n=bin(int(input()))[2:]
if n=='0':print(0)
elif '0' in n: print(-1)
else:print(n.count('1'))
