for _ in range(int(input())):
    word=input()
    answer=[word.count(x) for x in 'aeiou']
    print(f'The number of vowels in {word} is {sum(answer)}.')
