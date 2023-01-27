input()
word = input()
s=word.count('security')
b=word.count('bigdata')


if s>b: print('security!')
elif s<b: print('bigdata?')
else: print('bigdata? security!')

