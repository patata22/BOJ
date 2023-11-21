n=int(input())
x=input()
print('Yes') if x[:n//2]==x[n//2:] else print('No')
