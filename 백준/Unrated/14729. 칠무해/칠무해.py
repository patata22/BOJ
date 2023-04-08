import sys
input=sys.stdin.readline
for x in sorted([float(input()) for i in range(int(input()))])[:7]:
    print(f'{x:.3f}')
