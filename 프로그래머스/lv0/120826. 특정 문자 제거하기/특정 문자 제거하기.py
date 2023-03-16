def solution(my_string, letter):
    for x in letter:
        my_string = my_string.replace(x,'')
    return my_string