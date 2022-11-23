import os
from pyduinocoin import DuinoClient
from time import sleep

clear = lambda: os.system('clear') # os.system('cls') for Windows
client = DuinoClient()
username = input('Username: ')

try:
    result = client.user(username)
except Exception as error:
    print(error)
else:
    while True:
        print(username + "'s balance: " + str(round(result.balance.balance, 3)) + ' ᕲ')
        print(username + "'s miners: ")
        for miner in result.miners:
            print('- ' + miner.identifier + ': ' + str(miner.hashrate) + ' H/s')
        sleep(30)