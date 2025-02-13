import sys
input=sys.stdin.readline

for tt in range(int(input())):
   n=int(input())
   original=list(input().rstrip())
   stack=[]
   while original:
      stack.append(original.pop())
      while len(stack)>=3 and stack[-3]==stack[-2]=='B' and stack[-1]=='A':
         stack.pop()
         stack.pop()
         stack.pop()
         stack.append('A')
         original.append('B')
   print(''.join(stack[::-1]))
