import os
from pyduinocoin import DuinoClient
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

clear = lambda: os.system('clear') # os.system('cls') for Windows
client = DuinoClient()
username = input('Username: ')
c = 'r'
while c != 'q':
    clear()
    try:
        result = client.user(username)
    except Exception as error:
        print(error)
    else:
        print(bcolors.OKGREEN + username + "'s balance: " + bcolors.ENDC + str(round(result.balance.balance, 3)) + ' ᕲ')
        print(bcolors.OKGREEN + username + "'s miners: " + bcolors.ENDC)
        for miner in result.miners:
            print('- ' + miner.identifier + ': ' + str(miner.hashrate) + ' H/s')
        c = input(bcolors.WARNING + '(r)efresh / (q)uit: ' + bcolors.ENDC)
clear()
print(bcolors.BOLD + 'Developed by iTzNikolovich' + bcolors.ENDC)
        
