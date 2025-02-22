
def sol():
   global temp
   temp=temp.strip()
   if temp[:7]=='What is':
      print('Forty-two'+''.join(temp[4:])+'.')

temp=''
for x in input():
   if x=='.': temp=''
   elif x=='?':
      sol()
      temp=''
   else: temp+=x
