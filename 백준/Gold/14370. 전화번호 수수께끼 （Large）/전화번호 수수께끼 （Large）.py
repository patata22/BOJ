word={'Z':'ZERO', 'O':'ONE', 'W':'TWO', 'R':'THREE', 'F':'FOUR', 'V':'FIVE',
      'X':'SIX', 'S':'SEVEN', 'G':'EIGHT', 'I':'NINE'}
num={'Z':'0', 'O':'1', 'W':'2', 'R':'3', 'F':'4', 'V':'5',
     'X':'6', 'S':'7', 'G':'8', 'I':'9'}


for _ in range(int(input())):
    count=[0]*26
    for x in map(lambda x:ord(x)-65, input()):
        count[x]+=1
    
    answer=[]
    
    for key in 'ZXWSVGFROI':
        cnt=count[ord(key)-65]
        if not cnt: continue
        for __ in range(cnt): answer.append(num[key])
        w=word[key]
        for x in w: count[ord(x)-65]-=cnt
    answer.sort()
    print(f'Case #{_+1}: {"".join(answer)}')
    
        
