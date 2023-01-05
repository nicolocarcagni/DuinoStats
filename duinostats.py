import os
from pyduinocoin import DuinoClient
from time import sleep
import ctypes


HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
NL = '\n'

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW("Developed by iTzNikolovich")

client = DuinoClient()

clear()

def user():
    clear()
    print(f"{BOLD}{'=' * 10} DuinoStats {'=' * 10}{ENDC}")
    username = input(f"{BOLD}Username: {ENDC}")
    return username

choice = "r"
errors = 0
username = user()
while choice != 'q':
    clear()
    try:
        result = client.user(username)
    except Exception as error:
        choice = 'q'
        errors = 100
    else:
        miners = 0
        total_hashrate = 0
        print(f"{OKGREEN}{username}'s balance: {ENDC}{(round(result.balance.balance, 3))}{'ᕲ'}")
        print(f"{NL}{OKGREEN}{username}'s miners:{ENDC}")
        for miner in result.miners:
            print(f"- {miner.identifier}: {str(round((miner.hashrate/1000)))} kH/s")
            miners = miners + 1
            total_hashrate = (miner.hashrate + total_hashrate)
            if(miners > 0 and miner.rejected != 0):
                print(f"{FAIL}There are some rejected share, check {miner.identifier}{ENDC}")
        print(f"{BOLD}Total miners: {ENDC}{OKGREEN}{str(miners)}{ENDC}")
        if(miners > 0):
            print(f"{BOLD}Total hashrate: {ENDC}{OKGREEN}{(round(total_hashrate / 1000))} kH/s{ENDC}")
            print(f"{BOLD}Software: {ENDC}{OKGREEN}{miner.software}{ENDC}")
        
        choice = input(f"{WARNING}{NL}(r)efresh / (u)sername / (t)ransactions / (q)uit: {ENDC}")
        
        if choice == 'r':
            print(f"{WARNING}Please wait to avoid API overloading...{ENDC}")
            sleep(8)
        elif choice == 'u':
            username = user()
        elif choice == 'q':
            clear()
        elif choice == 't':
            clear()
            print(f"{BOLD}Last 5 transactions:{NL}{ENDC}")
            for transactions in result.transactions:
                    print(f"{BOLD}Recipient: {ENDC + OKGREEN + transactions.recipient + ENDC}")
                    print(f"{BOLD}Sender: {ENDC + OKGREEN + transactions.sender + ENDC}")
                    print(f"{BOLD}Date: {ENDC + OKGREEN + transactions.datetime + ENDC}")
                    print(f"{BOLD}Amount: {ENDC + OKGREEN + str(transactions.amount)}{' ᕲ'}{ENDC}")
                    print(f"{BOLD}Description: {ENDC + WARNING + transactions.memo + ENDC}")
                    print()
            choice = input(f"{WARNING}Press anything to go back or (q)uit: {ENDC}")
            if choice == 'q':
                break
        else:
            print(f"{FAIL}Bad choice. Please wait to avoid API overloading...{ENDC}")
            sleep(8)
            choice = 'r'

if errors != 0:
    print(FAIL + 'Error ', end='')
    if errors == 100:
        print('100: Check username or network')
        print(f"{WARNING}If the error persists check server status at: ", end='')
        print(f'https://status.duinocoin.com/{ENDC}')
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
print(f"{BOLD}{FAIL}{'=' * 5} Check iTzNikolovich's projects on GitHub {'=' * 5}{ENDC}")
