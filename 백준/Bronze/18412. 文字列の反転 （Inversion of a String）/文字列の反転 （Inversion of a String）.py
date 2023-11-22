n,a,b=map(int,input().split())
a-=1
b-=1
word=list(input())
word[a:b+1]=word[a:b+1][::-1]
print(''.join(word))
