import os; import pyperclip
from termcolor import colored
import colorama

colorama.init()

loopFlag = 0; decoyIter = 1

BANNER1 = colored('''
 ▓█████▄  ▒█████   ██▀███   ██ ▄█▀ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
 ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒  ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
 ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
 ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
 ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
  ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
  ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░    ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒''', 'blue')
BANNER2 = colored('''              -----------------------------------------------''', 'blue')
BANNER3 = colored('''              || DorkNinja: The Google Dork Term Generator ||''', 'red')
BANNER4 = colored('''              -----------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


if __name__ == '__main__':

    printBanner()

    while(True):
        dorkFinal = ""
        inputString = ""
        dorkFilterList = []
        dorkList = []

        print()

        while(True):
            inputString = input("Enter search term(s): ")
            if (inputString != ""):
                if (inputString.startswith("inurl:") or inputString.startswith("ext:")):
                    dorkFilterList.append(inputString)
                else:
                    dorkList.append(f"\"{inputString}\"")
            elif (inputString == ""):
                break
            dorkString = " AND ".join(dorkList)
            dorkString += " " + " ".join(dorkFilterList)
            dorkFinal = "intext:" + dorkString

        print("\nGoogle Dork term constructed: " + dorkFinal)
        pyperclip.copy(dorkFinal)
        print("\nCopied to clipboard, press Enter for another Dork.")
        input()

        clrscr()
