#this is the good one
import random


def get_fortune():
    # List of fortunes with a clear, descriptive name
    fortunes = [
        "You will be lucky!",
        "You will be nearly lucky!",
        "You will be unlucky!",
        "You will lose $20!",
        "You will write a letter to your boss!",
        "You will get a promotion!",
        "You will get a bonus!",
        "You will lose your job!",
        "You will get an internship!",
        "You will get a job!",
        "You will fail your course due to late work!",
        "You will sleep through all alarms!",
        "You will get a Bachelor's degree!",
        "You will get a Master's degree!",
        "Your partner will leave you!",
        "You will meet your future spouse in a line!"
    ]
    return random.choice(fortunes)


def is_legal_age(age):
    # Function to check if the user is of legal age (clean separation of logic)
    return age >= 18


def fortune_teller():
    # Greet and get input from the user
    print("Welcome to the Fortune Teller!")
    name = input("Please enter your name: ")

    print(f"Hello {name}, I will tell your fortune!")

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age entered. Please enter a valid number.")
        return

    if is_legal_age(age):
        print("I see that you are of legal age. Let's proceed to your fortune!")
        print(f"Your fortune is: {get_fortune()}")
        print(f"Thank you for using the fortune teller, {name}. Good luck!")
    else:
        print("You are not of legal age! Your future is not predictable yet.")
        print("You have been banished from the program.")

    # Ask if the user wants to play again
    repeat = input("Would you like to try again? (yes/no): ").lower()
    if repeat == "yes":
        fortune_teller()
    else:
        print("Goodbye! Thanks for using the fortune teller.")
        exit(0)


# Runs the fortune teller program
fortune_teller()
