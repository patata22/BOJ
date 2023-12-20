for _ in range(int(input())):
    answer=0
    seq=0
    for x in input().split():
        if x=='X':seq+=1
        else:
            answer=max(answer,seq)
            seq=0
    answer=max(answer,seq)
    print(f"The longest contiguous subsequence of X's is of length {answer}")
