"""Write a program to check a character is vowel or not."""

vowel = ['a','e','i','o','u']

letter= input("enter a character: ").lower()

if letter in vowel:
    print("Given character is vowel")
else:
    print("Given character is not vowel")
