def solution(arr):
    answer=0
    flag=True
    while flag:
        flag=False
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i]//=2
                flag=True
            elif arr[i]<50 and arr[i]%2:
                arr[i]=arr[i]*2+1
                flag=True
        answer+=1
    return answer-1