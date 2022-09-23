direct={'U':0, 'D':2, 'L':1, 'R':3}
items={}
monsters={}

dx=(-1,0,1,0)
dy=(0,-1,0,1)

def fight(monster):
    global lv,max_hp,hp,attack,defense,exp,weapon,armor,clear
    w,a,h,e=monster[1:]
    ATTACK = attack+weapon
    DEFENSE = defense+armor
    co=acc.count("CO")
    dx=acc.count("DX")
    while True:
        if co and dx:
            h-= max(1,3*ATTACK-a)
            co-=1
            dx-=1
            if h<=0:
                afterBattle(e)
                return True
        elif co:
            h-= max(1,2*ATTACK-a)
            co-=1
            if h<=0:
                afterBattle(e)
                return True
        else:
            h-=max(1,ATTACK-a)
            if h<=0:
                afterBattle(e)
                return True
        hp-=max(1,w-DEFENSE)
        if hp<=0:
            return False
            
def fight_boss(monster):
    global lv,max_hp,hp,attack,defense,exp,weapon,armor,clear
    
    w,a,h,e=monster[1:]
    ATTACK = attack+weapon
    DEFENSE = defense+armor
    co=acc.count("CO")
    dx=acc.count("DX")
    hu=acc.count("HU")
    if hu:hp=max_hp
    while True:
        if co and dx:
            h-= max(1,3*ATTACK-a)
            co-=1
            dx-=1
            if h<=0:
                afterBattle(e)
                return True
        elif co:
            h-= max(1,2*ATTACK-a)
            co-=1
            if h<=0:
                afterBattle(e)
                return True
        else:
            h-=max(1,ATTACK-a)
            if h<=0:
                afterBattle(e)
                return True
        if hu:hu-=1;
        else:
            hp-=max(1,w-DEFENSE)
            if hp<=0:
                return False

def afterBattle(e):
    global lv,max_hp,hp,attack,defense,exp,weapon,armor,clear
    if 'HR' in acc: hp = min(max_hp , hp+3)
    if 'EX' in acc: exp+=int(1.2*e)
    else: exp+=e
    if exp>=lv*5:
        lv+=1
        attack+=2
        defense+=2
        max_hp+=5
        hp=max_hp
        exp=0

def deathCheck():
    global lv,max_hp,hp,attack,defense,exp,weapon,armor,clear,x,y
    if 'RE' in acc:
        hp=max_hp
        x=start_x
        y=start_y
        acc.remove('RE')
        return False
    return True

n,m=map(int,input().split())
board=[]
k=0
b=0
start_x=0
start_y=0
x=0
y=0
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='@':
            x=i
            start_x=i
            y=j
            start_y=j
            temp[j]='.'
        elif temp[j]=='&':k+=1
        elif temp[j]=='B':b+=1
    board.append(temp)


commands=list(input())
for _ in range(k+1):
    r,c,name,w,a,h,e=input().split()
    if board[int(r)-1][int(c)-1]=='M':
        BOSS=(name, int(w), int(a), int(h), int(e))
    else:
        monsters[(int(r)-1,int(c)-1)]=(name, int(w), int(a), int(h), int(e))

for _ in range(b):
    r,c,t,s=input().split()
    items[(int(r)-1,int(c)-1)]=(t,s)

lv=1
max_hp=20
hp=20
attack=2
defense=2
exp=0
weapon=0
armor=0
acc=[]
clear=False

turn=0
killed=""

for command in commands:
    turn +=1
    nx,ny = x+dx[direct[command]], y+dy[direct[command]]
    if not (0<=nx<n and 0<=ny<m) or board[nx][ny]=='#':
        if board[x][y]=='^':
            if 'DX' in acc:hp-=1
            else: hp-=5
            if hp<=0:
                if deathCheck():
                    hp=0
                    killed="SPIKE TRAP"
                    break
    elif board[nx][ny]=='.':
        x,y=nx,ny
    elif board[nx][ny]=='^':
        if 'DX' in acc: hp-=1
        else: hp-=5
        if hp<=0:
            if deathCheck():
                hp=0
                killed="SPIKE TRAP"
                break
        else:x,y=nx,ny
    elif board[nx][ny]=='&':
        monster=monsters[(nx,ny)]
        win=fight(monster)
        if win:
            board[nx][ny]='.'
            x,y=nx,ny
        else:
            if deathCheck():
                hp=0
                killed=monster[0]
                break
    elif board[nx][ny]=='M':
        win=fight_boss(BOSS)
        if win:
            board[nx][ny]='.'
            x,y=nx,ny
            clear=True
            break
        else:
            if deathCheck():
                hp=0
                killed=BOSS[0]
                break
    elif board[nx][ny]=='B':
        item=items[(nx,ny)]
        x,y=nx,ny
        board[nx][ny]='.'
        if item[0]=='W':weapon=int(item[1])
        elif item[0]=='A':armor=int(item[1])
        else:
            if item[1] in acc or len(acc)>3:
                continue
            else: acc.append(item[1])
        
        
        
        
if hp>0: board[x][y]='@'
for i in range(n):print(*board[i],sep='')
print(f'Passed Turns : {turn}')
print(f'LV : {lv}')
print(f'HP : {hp}/{max_hp}')
print(f'ATT : {attack}+{weapon}')
print(f'DEF : {defense}+{armor}')
print(f'EXP : {exp}/{5*lv}')
if clear:print("YOU WIN!")
elif hp<=0:print(f"YOU HAVE BEEN KILLED BY {killed}..")
else: print("Press any key to continue.")
