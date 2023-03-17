def solution(numbers, hand):
    
    answer = ''
    
    left=set([1,4,7])
    right=set([3,6,9])
    location={}
    for i in range(9):
        location[i+1]= (i//3, i%3)
        
    location[0]=(3,1)
    leftNow= (3,0)
    rightNow=(3,2)
    
    for number in numbers:
        if number in left:
            leftNow=location[number]
            answer+='L'
        elif number in right:
            rightNow=location[number]
            answer+='R'
        else:
            leftDistance= getDistance(location[number], leftNow)
            rightDistance= getDistance(location[number], rightNow)
            if leftDistance<rightDistance:
                leftNow = location[number]
                answer+='L'
            elif rightDistance<leftDistance:
                rightNow = location[number]
                answer+='R'
            else: 
                if hand=='left':
                    leftNow = location[number]
                    answer+='L'
                else:
                    rightNow = location[number]
                    answer+='R'
                    
    return answer

def getDistance(button,now):
    x1,y1=button
    x2,y2=now
    return abs(x1-x2)+abs(y1-y2)