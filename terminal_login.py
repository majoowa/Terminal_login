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