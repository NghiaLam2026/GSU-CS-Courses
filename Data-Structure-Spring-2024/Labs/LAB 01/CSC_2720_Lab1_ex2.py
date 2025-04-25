import math 
#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:00 PM
#Due time: 01/14/2024 @ 11:59PM

#EXERCISE 2
def Guess_my_number():
    n = int(input("Enter n: "))
    while n <= 0:
        n = int(input("Enter a positive integer for n: "))

    print("Welcome to Guess My Number!", "\n"f"Please think of a number between 0 and {n - 1}.")

    #Initialized the lower and upper bounds for the guessing range.
    low = 0
    high = n

    while low <= high:
        middle_point = low + math.ceil(high - low) // 2 #Calculating the middle point, roudning up, to guess the number.
        print(f"Is your number {middle_point}?")
        print("Please enter C for correct, H for too high, or L for too low.")
        my_input = input("Enter your resposne (H/L/C): ")

        while my_input not in ["H", "L", "C"]:
            my_input = input("Enter your response (H/L/C): ")

        if my_input == "C":
            print("Thank you for playing Guess My Number!")
            break
        elif my_input == "H": #If the guess is too high, adjust the upper bound of the guessing range.
            high = middle_point - 1
        elif my_input == "L": #If the guess is too low, adjust the lower bound of the guessing range.
            low = middle_point + 1

Guess_my_number()
