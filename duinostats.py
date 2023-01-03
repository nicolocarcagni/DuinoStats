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

client = DuinoClient()\

clear()

c = 'r'
e = 0

username = input('Username: ')
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
        c = input(bcolors.WARNING + '(r)efresh / (u)sername / (q)uit: ' + bcolors.ENDC)
        
        if c == 'r':
            print(bcolors.WARNING + '\nPlease wait to avoid API overloading...' + bcolors.ENDC)
            sleep(8)

        if c == 'u':
            clear()
            username = input('Username: ')

if e != 0:
    print(bcolors.FAIL + 'Error ', end='')
    if e == 100:
        print('100: Check username or network')
        print(bcolors.WARNING + 'If the error persists check server status at: ', end='')
        print('https://status.duinocoin.com/' + bcolors.ENDC)
        sleep(4)
    else:
        print('Please try again in a while...' + bcolors.ENDC)
        sleep(0.5)
        print(bcolors.WARNING + 'If the error persists check server status: ', end='')
        print('https://status.duinocoin.com/' + bcolors.ENDC)
        sleep(4)

clear()

print(bcolors.BOLD + 'Consider donating some DUCOs: ' + bcolors.ENDC + bcolors.OKGREEN + 'Nikolovich' + bcolors.ENDC)
print(bcolors.BOLD + '\n====== Developed with ❤️  by iTzNikolovich ======\n' + bcolors.ENDC)
