import random
from user import User

def main():

    while True:
         print("Gracias welcome to pass-locker!!!!")
         print('\n')
         print("select a short code to navigate through:to create new user use'nu':To login to your account 'lg' or 'ex' to exit the locker")
         short_code = input().lower()
         print('\n')

         if short_code == 'nu':
            print('create username')
            created_user_name = input()
             
         print('create password')
            created_user_password = input()
            print('confirm password')
            confirm_password = input()


        else:
            print(f"congratulations (created_user_name)! account creation successful")
            print('\n')
            print("proceed to login")
            print("Username")
            entered_username = input()
            print("Your Password")
            entered_password = input()






if __name__ == "__main__":
    main()