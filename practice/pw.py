# -*- coding: UTF-8 -*-
#! python3
"""
密码箱
"""
import sys
import pyperclip

PASSWORDS = {
    'email': 'a',
    'blog': 'fdsafdafdasfdas',
    'luggage': '123456'
}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()


account = sys.argv[1] # first command line arg is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
