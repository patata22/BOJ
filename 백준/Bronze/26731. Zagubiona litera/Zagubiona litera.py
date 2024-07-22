count=[0]*26
for x in input():
    count[ord(x)-65]=1
for i in range(26):
    if not count[i]: print(chr(i+65))
