import requests
import ipapi
from colorama import Fore, init
import time
import os
import platform
import getpass
init()
# created by Ali Garivani


def check_location():
    os_name = platform.uname()[0]
    print(Fore.LIGHTMAGENTA_EX+'Start Resived Ip')
    ip_client = requests.get('https://api.ipify.org').text

    print(Fore.LIGHTMAGENTA_EX+'search your location ...')
    location_client = ipapi.location(ip_client)['country']
    time.sleep(0.5)
    print(Fore.LIGHTMAGENTA_EX+'Search Your city ...')
    city = ipapi.location(ip_client)['region']
    time.sleep(0.5)
    print(Fore.LIGHTMAGENTA_EX+'Done')
    time.sleep(1)
    if os_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    if location_client == 'IR':
        print(Fore.RED+'[*] '+Fore.LIGHTCYAN_EX+'sorry you location' +
              Fore.LIGHTRED_EX+' Iran '+Fore.LIGHTCYAN_EX+'please use vpn '.format(city))
    else:
        print(Fore.GREEN+'[*] '+Fore.LIGHTCYAN_EX+'so your location' +
              Fore.LIGHTGREEN_EX+f' {city} '+Fore.LIGHTCYAN_EX+'is good you full acsess '+Fore.WHITE)
    input('press eny key for back to menu ')
    menu()


def show_system():
    ip_client = requests.get('https://api.ipify.org').text
    status = platform.uname()
    print('\n'+'[*] '+Fore.BLUE+'your os : ' +
          Fore.GREEN+f'{status[0]}'+Fore.WHITE+'\n')
    print('[*] '+Fore.BLUE+'version os : ' +
          Fore.GREEN+f'{status[2]}'+Fore.WHITE+'\n')
    print('[*] '+Fore.BLUE+'user name : '+Fore.GREEN +
          f'{getpass.getuser()}'+Fore.WHITE+'\n')
    print('[*] '+Fore.BLUE+'Ip system : ' +
          Fore.GREEN+f'{ip_client}'+Fore.WHITE+'\n'+Fore.WHITE)
    input('press eny key for back to menu ')
    menu()


def admin_finder():
    http = input(Fore.CYAN+' http ' + Fore.WHITE+'enter'+Fore.CYAN+" 1 " + Fore.WHITE +
                 'or'+Fore.GREEN+' https ' + Fore.WHITE+'enter'+Fore.GREEN+" 2 "+Fore.WHITE+':  ')

    if http == '1':
        http = 'http'
    elif http == '2':
        http = 'https'

    address = input("enter address site "+Fore.GREEN +
                    "('google.come')"+Fore.WHITE+" : ")

    admin_list = ['admin/', 'administrator/', 'login.php', 'administration/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/',
                  'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp', 'admin/login.asp', 'admin/admin.asp', '/login.aspx',
                  'admin_area/admin.asp', 'admin_area/login.asp', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
                  'admin_area/admin.html', 'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp', 'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp',
                  'bb-admin/index.html']

    for item in admin_list:
        url = requests.get(f'{http}://{address}/{item}').status_code

        if url == 200:
            print(Fore.GREEN + f'{http}://{address}/{item} ',
                  Fore.GREEN+str(" admin page True :) "))
        elif url == 402:
            print(Fore.RED + f'{http}://{address}/{item} ',
                  Fore.YELLOW+' acsess denied')
        elif url == 404:
            print(Fore.RED + f'{http}://{address}/{item} ',
                  Fore.RED + ' this addresss not True :( '+Fore.WHITE)
    input('press eny key for back to menu ')
    menu()


def menu():
    os_name = platform.uname()[0]
    if os_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    print(Fore.CYAN+'[1] '+Fore.RED+'check location')
    print(Fore.CYAN+'[2] '+Fore.RED+'show system status')
    print(Fore.CYAN+'[3] '+Fore.RED+'admin finder'+Fore.WHITE)
    print(Fore.CYAN+'[4] '+Fore.RED+'Exit'+Fore.WHITE)
    inp = input('--> ')
    if inp == '1':
        check_location()
    elif inp == '2':
        show_system()
    elif inp == '3':
        admin_finder()
    elif inp == '4':
        quit()
    else:
        menu()


menu()
