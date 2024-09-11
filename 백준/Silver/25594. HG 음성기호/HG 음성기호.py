def sol():
    now=0
    answer=[]
    while now<len(original):
        head = original[now]
        idx = ord(head)-97
        l=len(word[idx])
        if original[now:now+l]==word[idx]:
            answer.append(head)
            now+=l
        else:
            print('ERROR!')
            return
    print("It's HG!")
    print(''.join(answer))
        
original=input()
word=['aespa', 'baekjoon', 'cau', 'debug', 'edge', 'firefox', 'golang', 'haegang', 'iu', 'java', 'kotlin', 'lol', 'mips', 'null', 'os', 'python', 'query', 'roka', 'solvedac', 'tod', 'unix', 'virus', 'whale', 'xcode', 'yahoo', 'zebra']
sol()
