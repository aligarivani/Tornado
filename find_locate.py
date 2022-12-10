import requests
import ipapi
from colorama import Fore, init

init()

ip_client = requests.get('https://api.ipify.org').text
location_client = ipapi.location(ip_client)['country']
city = ipapi.location(ip_client)['region']
if location_client == 'IR':
    print(Fore.RED+'[*] '+Fore.LIGHTCYAN_EX+'sorry you location' +
          Fore.LIGHTRED_EX+f' {city} '+Fore.LIGHTCYAN_EX+'please use vpn '.format(city))
else:
    print(Fore.GREEN+'[*] '+Fore.LIGHTCYAN_EX+'so your location' +
          Fore.LIGHTGREEN_EX+f' {city} '+Fore.LIGHTCYAN_EX+'is good you full acsess ')