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
