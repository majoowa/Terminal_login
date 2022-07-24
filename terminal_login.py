import platform
import os
import time

menu_option = str()
login = str()
password = str()
password_confirmation =str()
time_sleep = 5.0


login_details_dict ={"kate":"password1", "henry":"password2"}

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    
def delete_user():
    trial=1
    print("Confirm your login details\nLogin:")
    login=input()
    if login in login_details_dict.keys():
        print("Password:")
        password = input()
        while password != login_details_dict[login] and trial<= 3:
            trial +=1
            print("Password is wrong, try again, you still have " +str(5-trial) + " chances to delete your account")
            password =input()
            if trial > 3:
                print("Maybe you don't want to delete your account? You entered the password incorrectly too many times. You will be taken to your profile in a second")
                time.sleep(time_sleep)
                user_profile()
                menu()
        if password == login_details_dict[login] and trial <=3:
            login_details_dict.pop(login)
            print("Your account is deleted, you will be taken to menu option in a second")
            time.sleep(time_sleep)
            menu()
    elif login not in login_details_dict.keys():
        print("This login is wrong or not exist, try again:")
        delete_user()

def exit():
    clear_console()
    print("See you soon!")
    
def log_in():
    clear_console()
    trial = 1
    print("Enter your login details:\nLogin:")
    login = input()
    if login in login_details_dict.keys():
        print("Password:")
        password = input()
        while password != login_details_dict[login] and trial<= 3:
            trial +=1
            print("Password is wrong, try again, you still have " +str(5-trial) + " chances to log in")
            password =input()
            if trial > 3:
                print("Sorry, you have to start everything ones again, you will be taken to menu option in a second")
                time.sleep(time_sleep)
                clear_console()
                menu()
        if password == login_details_dict[login] and trial <=3:
            user_profile()
    elif login not in login_details_dict.keys():
        print("This login is wrong or not exist. Choose what you want to do now?\n1. Try log in again\n2. Sign up\n3. Exit")
        action = input()
        if action == "1":
            log_in()
        elif action == "2":
            sign_up()
        elif action == "3":
            exit()
        else:
            while action != "1" or action != "2" or action !="3":
                print("Wrong answer. Choose one option:\n1. Log in\n2. Sign up\n3. Exit")
                action = input()
                if action == "1":
                    log_in()
                elif action == "2":
                    sign_up()
                elif action == "3":
                    exit()
        

def sign_up():
    clear_console()
    trial = 1
    len_trial=1
    print("Enter your sign up details:\nLogin:")
    login = input()
    if login in login_details_dict.keys():
        print("This login already exists, try again:")
        time.sleep(time_sleep)
        sign_up()
    else:
        print("Password:\n *remember password should consist of minimum 6 signs")
        password = input()
        while len(password) < 6 and len_trial<=3:
            len_trial +=1
            print("Your password is less than 6 signs, type password again:")
            password = input()
            if len_trial > 3:
                print("Your password should consist of minimum 6 signs. You entered too short password too many times. Start from the beginning")
                time.sleep(time_sleep)
                sign_up()
        print("Confirm password:")
        password_confirmation = input()
        if password_confirmation != password:
            while password_confirmation != password and trial<= 3:
                trial +=1
                print("Passwords are different, type password confirmation once again, you still have " +str(5-trial) + " chances to sign up")
                password_confirmation =input()
                if password_confirmation == password and trial <=3:
                    login_details_dict[login] = password
                    user_profile()
                elif trial > 3:
                    print("Sorry, you have to start everything ones again, you will be taken to menu option in a second")
                    time.sleep(time_sleep)
                    clear_console()
                    menu()
        elif password_confirmation == password:
            login_details_dict[login] = password
            print(login_details_dict)
            user_profile()
                

def user_profile():
    clear_console()
    print("What do we do now?\n1. Log out\n2. Delete account")
    user_answer = input()
    if user_answer == "1":
        menu()
    elif user_answer == "2":
        print("Are you sure, you want to delete your account? Yes or No?")
        delete_confirmation = input().capitalize()
        if delete_confirmation == "Yes":
            delete_user()
            time.sleep(time_sleep)
            menu()
        elif delete_confirmation =="No":
            user_profile()
        else:
            while delete_confirmation != "Yes" or delete_confirmation != "No":
                print("Wrong answer, try again")
                delete_confirmation = input().capitalize()
                if delete_confirmation == "Yes":
                    delete_user()
                    print("Your account is deleted, you will be taken to menu option in a second")
                    time.sleep(time_sleep)
                    menu()
                elif delete_confirmation =="No":
                    user_profile()
    
        
def menu():
    clear_console()
    print("Hello, what do you want to do? Choose one option:\n1. Log in\n2. Sign up\n3. Exit")
    menu_option = input()
    if menu_option == "1":
        log_in()
    elif menu_option == "2":
        sign_up()
    elif menu_option == "3":
        clear_console()
        print("See you soon!")
    else: 
        print("Wrong answer! What do you want to do? Try again in a second")
        time.sleep(time_sleep)
        menu()
    
menu() #starts program