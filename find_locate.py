import requests
import ipapi
from colorama import Fore, init
import time
import os
import platform
init()
# created by Ali Garivani
os_name = platform.uname()[0]


def find():
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
              Fore.LIGHTGREEN_EX+f' {city} '+Fore.LIGHTCYAN_EX+'is good you full acsess ')
    print(city)


find()
