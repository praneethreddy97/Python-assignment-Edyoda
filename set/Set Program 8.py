#8.Python – Program to accept the strings which contains all vowels

def vowels_check(input_word):
    input_word=input_word.lower()

    vowels='aeiou'
    for check in vowels:
        if check not in input_word:
            return False
    return True


word=input("enter a word")

if vowels_check(word):
    print("it contain all vowels")
else:
    print("it does not contain all vowels")
