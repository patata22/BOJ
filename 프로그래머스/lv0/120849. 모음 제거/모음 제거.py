def solution(my_string):
    for x in ('a','e','i','o','u'):
        my_string=my_string.replace(x,'')
    return my_string