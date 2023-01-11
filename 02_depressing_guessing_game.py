# 02_GuessingGame_JoeyEdition

number = int(input("I am thinking on a number between 1 and 10. Can you guess which is it? "))

if number < 0 or number > 10:
    print("Sorry, invalid number.")
if number > 8 and number < 11:
    print("Sorry, I was thinking of " + str(number-2) + ".")
if number >= 0 and number <= 8:
    print("Sorry, I was thinking of " + str(number+2) + ".")
