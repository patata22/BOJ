name=[input(),input()]
point=[0,0]
turn=0
input()
for x in input():
    
    if x=='H':
        point[turn]+=1
        
        if point[turn]==7:break
    elif x=='D':
        point[turn]=min(7,point[turn]+2)
        if point[turn]==7:break
    elif x=='O':
        point[1-turn]+=1
        if point[1-turn]==7:
            turn=1-turn
            break
    turn=1-turn

print(f'{name[0]} {point[0]} {name[1]} {point[1]}.',end=' ')
if point[turn]==7:print(f'{name[turn]} has won.')
else:
    if point[0]>point[1]:print(f'{name[0]} is winning.')
    elif point[0]<point[1]:print(f'{name[1]} is winning.')
    else: print('All square.')
    