import platform
import os

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def menu():
    clear_console()
    print("Hello, what do you want to do? Choose one option:\n1. Log in\n2. Sign up\n3. Exit")

def log_in():
    clear_console()
    print("Enter your login details:\nLog in:")
    print("Password:")

def sign_up():
    clear_console()
    print("Enter your sign up details:\nLogin:")
    print("Password:")
    print("Confirm password:")

def user_profile():
    clear_console()
    print("What do we do now?\n1. Log out\n2. Delete account")