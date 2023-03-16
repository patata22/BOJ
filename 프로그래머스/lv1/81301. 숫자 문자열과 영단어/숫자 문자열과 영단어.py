def solution(s):
    change={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0"}
    for x in change:
        s=s.replace(x, change[x])
    return int(s)