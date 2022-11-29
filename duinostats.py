import os
from pyduinocoin import DuinoClient
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

clear = lambda: os.system('clear') # os.system('cls') on Windows Systems
client = DuinoClient()
username = input('Username: ')
c = 'r'
e = 0
while c != 'q':
    clear()
    try:
        result = client.user(username)
    except Exception as error:
        c = 'q'
        e = 100
    else:
        print(bcolors.OKGREEN + username + "'s balance: " + bcolors.ENDC + str(round(result.balance.balance, 3)) + ' ᕲ')
        print(bcolors.OKGREEN + username + "'s miners: " + bcolors.ENDC)
        for miner in result.miners:
            print('- ' + miner.identifier + ': ' + str(miner.hashrate) + ' H/s')
        c = input(bcolors.WARNING + '(r)efresh / (q)uit: ' + bcolors.ENDC)

if e != 0:
    if e == 100:
        print(bcolors.FAIL + 'Error 100: Check that the entered data is correct' + bcolors.ENDC)
        sleep(3)

clear()
print(bcolors.BOLD + 'Developed by iTzNikolovich' + bcolors.ENDC)
        
