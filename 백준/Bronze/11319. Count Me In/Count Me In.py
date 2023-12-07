vowel='aeiouAEIOU'
for _ in range(int(input())):
    con=0
    vow=0
    text=input()
    for x in text:
        if x==' ': continue
        if x in vowel: vow+=1
        else: con+=1
    print(con, vow)
