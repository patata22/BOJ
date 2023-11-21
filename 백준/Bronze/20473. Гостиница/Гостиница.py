n=int(input())
three=n//3
n%=3
if n%2:
    three-=1
    n+=3
print(n//2,three)