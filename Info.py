#!/usr/bin/python
#chat bot
#tegar ID

# import libraries
from os import system as bodoamat
from time import sleep as waktu
import json
import pyfiglet
import sys

# nginstall bahan
try:
    import requests
except ImportError:
    print('install dulu libraries requests nya')
    input('[<EnterTo Install>]')
    bodoamat('pip install requests')

def banner():
    print('\033[34;1m')
    logo = pyfiglet.figlet_format('Mr-Robot')
    print(logo)
    print('\t\033[37;1m[\033[41;1m Phone Information \033[00;1m\033[37;1m ]\n')
    print('\033[32;1mCreator \033[37;1m: \033[33;1mSayyed-Zakarya')
    print('\033[32;1mVersion \033[37;1m: \033[33;1m1.0')

def lacak():
    bodoamat('clear')
    banner()
    print(50*'\033[33;1m=')
    print('')
    print('\t\033[37;1m[\033[31;1m!\033[37;1m]\033[34;1mEnter Number Ex. \033[37;1m: \033[37;1m92345xxxx\n')
    no = input('\t\033[34;1mNumber \033[37;1m: \033[32;1m')
    link = 'https://api.veriphone.io/v2/verify?phone={}&key=5F3F2D6300E445DEA88684053144966C'.format(no)
    req = requests.get(link)
    jeson = json.loads(req.text)
    print('\t\033[31;1mphone         \033[37;1m: \033[32;1m', jeson['phone'])
    print('\t\033[31;1mtype          \033[37;1m: \033[32;1m', jeson['phone_type'])
    print('\t\033[31;1mregion        \033[37;1m: \033[32;1m', jeson['phone_region'])
    print('\t\033[31;1mcountry       \033[37;1m: \033[32;1m', jeson['country'])
    print('\t\033[31;1mcode          \033[37;1m: \033[32;1m', jeson['country_code'])
    print('\t\033[31;1mprefix        \033[37;1m: \033[32;1m', jeson['country_prefix'])
    print('\t\033[31;1minternational \033[37;1m: \033[32;1m', jeson['international_number'])
    print('\t\033[31;1mlocal         \033[37;1m: \033[32;1m', jeson['local_number'])
    print('\t\033[31;1me164          \033[37;1m: \033[32;1m', jeson['e164'])
    print('\t\033[31;1mcarrier       \033[37;1m: \033[32;1m', jeson['carrier'])
    print(50*'\033[33;1m=')
    ulang = input('\033[31;1m[<Repeat>] \033[37;1m(y/n)')
    if ulang == 'y' or ulang == 'Y':
        bodoamat('python Info.py')
    elif ulang == 'n' or ulang == 'N':
        bodoamat('clear')
        sys.exit('\033[33;1mExit')
    else:
        bodoamat('clear')
        sys.exit('\033[33;1mExit')

lacak()
