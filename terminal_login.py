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