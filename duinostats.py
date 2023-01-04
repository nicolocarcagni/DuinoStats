import os
from pyduinocoin import DuinoClient
from time import sleep


HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
NL = '\n'

clear = lambda: os.system('clear') # os.system('cls') on Windows Systems

client = DuinoClient()\

clear()

c = 'r'
e = 0
print(f"{OKGREEN}{BOLD}== Developed by iTzNikolovich =={ENDC}")
print(f"{BOLD}{'=' * 10} DuinoStats {'=' * 10}{ENDC}")
print(f"{FAIL}{BOLD}== Developed by iTzNikolovich ==\n{ENDC}")
username = input(f"{BOLD}Username: {ENDC}")
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
        print(f"{OKGREEN}{username}'s balance: {ENDC}{(round(result.balance.balance, 3))}{'ᕲ'}")
        print(f"{NL}{OKGREEN}{username}'s miners:{ENDC}")
        for miner in result.miners:
            print(f"- {miner.identifier}: {str(round((miner.hashrate/1000)))} kH/s")
            n = n + 1
            h = (miner.hashrate + h)
            if(n > 0 and miner.rejected != 0):
                print(f"{FAIL}There are some rejected share, check {miner.identifier}{ENDC}")
        print(f"{BOLD}Total miners: {ENDC}{OKGREEN}{str(n)}{ENDC}")
        if(n > 0):
            print(f"{BOLD}Total hashrate: {ENDC}{OKGREEN}{(round(h / 1000))} kH/s{ENDC}")
            print(f"{BOLD}Software: {ENDC}{OKGREEN}{miner.software}{ENDC}")
        
        c = input(f"{WARNING}{NL}(r)efresh / (u)sername / (t)ransactions / (q)uit: {ENDC}")
        
        if c == 'r':
            print(f"{WARNING}Please wait to avoid API overloading...{ENDC}")
            sleep(8)
        elif c == 'u':
            clear()
            print(f"{OKGREEN}{BOLD}== Developed by iTzNikolovich =={ENDC}")
            print(f"{BOLD}{'=' * 10} DuinoStats {'=' * 10}{ENDC}")
            print(f"{FAIL}{BOLD}== Developed by iTzNikolovich ==\n{ENDC}")
            username = input(f"{BOLD}Username: {ENDC}")
        elif c == 'q':
            clear()
        elif c == 't':
            clear()
            print(f"{BOLD}Last 5 transactions:{NL}{ENDC}")
            for transactions in result.transactions:
                    print(f"{BOLD}Recipient: {ENDC}{OKGREEN}{transactions.recipient}{ENDC}")
                    print(f"{BOLD}Sender: {ENDC}{OKGREEN}{transactions.sender}{ENDC}")
                    print(f"{BOLD}Date: {ENDC}{OKGREEN}{transactions.datetime}{ENDC}")
                    print(f"{BOLD}Amount: {ENDC}{OKGREEN}{transactions.amount}{'ᕲ'}{ENDC}")
                    print(f"{BOLD}Description: {ENDC}{WARNING}{transactions.memo}{ENDC}")
                    print()
            c = input(f"{WARNING}Insert anything to close: {ENDC}")
            print(f"{WARNING}Please wait to avoid API overloading...{ENDC}")
            sleep(8)
        else:
            print(f"{FAIL}Bad choice. Please wait to avoid API overloading...{ENDC}")
            sleep(8)
            c = 'r'

if e != 0:
    print(FAIL + 'Error ', end='')
    if e == 100:
        print('100: Check username or network')
        print(WARNING + 'If the error persists check server status at: ', end='')
        print('https://status.duinocoin.com/' + ENDC)
        sleep(2)
    else:
        print('Please try again in a while...' + ENDC)
        sleep(0.5)
        print(WARNING + 'If the error persists check server status: ', end='')
        print('https://status.duinocoin.com/' + ENDC)
        sleep(2)

clear()

print(f"{BOLD}{OKGREEN}{'=' * 5} Consider donating some DUCOs: Nikolovich {'=' * 5}{ENDC}")
print(f"{BOLD}{'=' * 12} Developed with ❤️  in Italy {'=' * 12}{ENDC}")
