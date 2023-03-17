def solution(a, b):
    day=("FRI","SAT","SUN","MON","TUE","WED","THU")
    month={1:0, 2:31, 3:29, 4:31, 5:30, 6:31, 7:30, 8:31, 9:31, 10:30, 11:31, 12:30}
    for i in range(1,a+1):
        b+=month[i]
    b%=7
    answer = day[b-1]
    
    return answer