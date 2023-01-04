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
print(bcolors.OKGREEN + '==Developed by iTzNikolovich==' + bcolors.ENDC)
print(bcolors.BOLD + '==========DuinoStats==========' + bcolors.ENDC)
print(bcolors.FAIL + '==Developed by iTzNikolovich==\n' + bcolors.ENDC)
username = input('Username: ')
while c != 'q':
    clear()
    try:
        result = client.user(username)
    except Exception as error:
        c = 'q'
        e = 100
    else:
        n = 0
        h = 0
        print(bcolors.OKGREEN + username + "'s balance: " + bcolors.ENDC + str(round(result.balance.balance, 3)) + ' ᕲ')
        print('\n' + bcolors.OKGREEN + username + "'s miners: " + bcolors.ENDC)
        for miner in result.miners:
            print('- ' + miner.identifier + ': ' + str(round((miner.hashrate/1000))) + ' kH/s')
            n = n + 1
            h = (miner.hashrate + h)
            if(n > 0 and miner.rejected != 0):
                print(bcolors.FAIL + 'There are some rejected share, check ' + miner.identifier + bcolors.ENDC)
        print(bcolors.BOLD + 'Total miners: ' + bcolors.ENDC + bcolors.OKGREEN + str(n) + bcolors.ENDC)
        print(bcolors.BOLD + 'Total hashrate: ' + bcolors.ENDC + bcolors.OKGREEN + str(round(h / 1000)) + 'kH/s' + bcolors.ENDC)
        if(n > 0):
            print(bcolors.BOLD + 'Software: ' + bcolors.ENDC + bcolors.OKGREEN + miner.software + bcolors.ENDC)
        
        c = input(bcolors.WARNING + '\n(r)efresh / (u)sername / (t)ransactions / (q)uit: ' + bcolors.ENDC)
        
        if c == 'r':
            print(bcolors.WARNING + '\nPlease wait to avoid API overloading...' + bcolors.ENDC)
            sleep(8)
        elif c == 'u':
            clear()
            username = input('Username: ')
        elif c == 'q':
            clear()
        elif c == 't':
            clear()
            print(bcolors.BOLD + 'Last 3 transactions:\n' + bcolors.ENDC)
            i = 0
            for transactions in result.transactions:
                while i < 3:
                    print(bcolors.BOLD + 'Recipient: ' + bcolors.ENDC + bcolors.OKGREEN + transactions.recipient + bcolors.ENDC)
                    print(bcolors.BOLD + 'Sender: ' + bcolors.ENDC + bcolors.OKGREEN + transactions.sender + bcolors.ENDC)
                    print(bcolors.BOLD + 'Date: ' + bcolors.ENDC + bcolors.OKGREEN + transactions.datetime + bcolors.ENDC)
                    print(bcolors.BOLD + 'Amount: ' + bcolors.ENDC + bcolors.OKGREEN + str(transactions.amount) + bcolors.ENDC)
                    print(bcolors.BOLD + 'Description: ' + bcolors.ENDC + bcolors.WARNING + str(transactions.memo) + bcolors.ENDC)
                    print()
                    i = i + 1
            c = input(bcolors.WARNING + 'Insert anything to close: ' + bcolors.ENDC)
            print(bcolors.WARNING + 'Please wait to avoid API overloading...' + bcolors.ENDC)
            sleep(8)
        else:
            print(bcolors.FAIL + 'Bad choice. Please wait to avoid API overloading...' + bcolors.ENDC)
            sleep(8)
            c = 'r'

if e != 0:
    print(bcolors.FAIL + 'Error ', end='')
    if e == 100:
        print('100: Check username or network')
        print(bcolors.WARNING + 'If the error persists check server status at: ', end='')
        print('https://status.duinocoin.com/' + bcolors.ENDC)
        sleep(2)
    else:
        print('Please try again in a while...' + bcolors.ENDC)
        sleep(0.5)
        print(bcolors.WARNING + 'If the error persists check server status: ', end='')
        print('https://status.duinocoin.com/' + bcolors.ENDC)
        sleep(2)

clear()

print(bcolors.BOLD + 'Consider donating some DUCOs: ' + bcolors.ENDC + bcolors.OKGREEN + 'Nikolovich' + bcolors.ENDC)
print(bcolors.BOLD + '\n====== Developed with ❤️  by iTzNikolovich ======\n' + bcolors.ENDC)
