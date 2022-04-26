#!/usr/bin/env python3.8
from credentials import Credentials
from user import User

def create_account(acc_name, user_name, user_password):
    new_account= Credentials(acc_name, user_name, user_password)
    return new_account


def save_credential (credentials):
    '''
    Function to delete a credentials
    '''
    credentials.save_credential()
def find_credential(acc_name):
    """
    find a credential from the credential list using account
    """
    return Credentials.find_credential(acc_name)
def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()


def del_account(Credentials):
    '''
    Function to delete an account
    '''
    Credentials.delete_account()
def main():
    print("Hello Welcome to your password locker site. What is your name?")
    name = input()
    print('\n')
    print(f"Hello {name}. what would you like to do?")
    print('\n')


    while True:
        print("Hello. Welcome back to Password Locker!")
        print('\n')
        print('Create a login username and a password')
        print('\n')
        print('Enter username')
        username =  input()
        print('Enter password')
        user_password = input()

        print('To login in, Enter your username')
        input_username = input()
        if (input_username == username):
            print('Enter your password')
            input_password = input()