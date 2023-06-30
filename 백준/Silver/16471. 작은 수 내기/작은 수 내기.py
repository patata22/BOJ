def sol():
    for i in range(target):
        if me[i]>=opp[i]:
            return "NO"
    return 'YES'

n=int(input())
target=n//2+1

me=sorted(list(map(int,input().split())))
opp=sorted(list(map(int,input().split())))[-target:]

print(sol())
