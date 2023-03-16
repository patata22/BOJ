def solution(numbers):
    word=("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    for i in range(10):
        numbers=numbers.replace(word[i],str(i))
    return int(numbers)