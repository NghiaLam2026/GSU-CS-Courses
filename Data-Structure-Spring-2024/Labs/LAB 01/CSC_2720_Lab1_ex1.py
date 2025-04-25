#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:00 PM
#Due time: 01/14/2024 @ 11:59PM

#EXERCISE 1
def Personalized_Hello_World():
    print("What is your name? ")
    while True:
        user_input = input("Please enter your name: ")
        if user_input == "":
            continue
        else:
            print(f"Hello, {user_input}!")
            break
Personalized_Hello_World()

