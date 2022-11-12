from selenium.webdriver.common.keys import Keys as keys
from webbrowser import open
from selenium import webdriver as wd
from time import sleep
from enum import Enum
import json
import core

BANNER:str=r"""
 ________   ___  ___  ___  __    _______      
|\   ___  \|\  \|\  \|\  \|\  \ |\  ___ \     
\ \  \\ \  \ \  \\\  \ \  \/  /|\ \   __/|    
 \ \  \\ \  \ \  \\\  \ \   ___  \ \  \_|/__  
  \ \  \\ \  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
   \ \__\\ \__\ \_______\ \__\\ \__\ \_______\
    \|__| \|__|\|_______|\|__| \|__|\|_______|
                                        valtyr
"""

DEFAULT_CONFIG:str='{"init": true, "browser": {"chrome": false, "firefox": false}, "sites": {"reddit": false, "twitter": false}, "payload": {"posts": false, "comments": false}}'

class site(Enum):
    WEBPAGE_REDDIT:str = "https://www.reddit.com"
    WEBPAGE_TWITTER:str = "https://twitter.com/home"

class driver(Enum):
    CHROME:str = "https://chromedriver.chromium.org/downloads"
    FIREFOX:str = "https://github.com/mozilla/geckodriver/releases"

class payload(Enum):
    POSTS:str = "POSTS"
    COMMENTS:str = "COMMENTS"


def choice():
    ...



if __name__=="__main__":
    print(BANNER)

    config = json.loads(core.read(path="config.json",arg="r"))

    if config['init'] == True:
        print("""Looks like this is your first time using this tool...\nSo here's how it works.\n\t- Select which browser you normally use from the menu.\n\t- Select which sites you want to nuke.\n\t- Select what you want to nuke.\n\t- Download and install the web driver from the window that opens after saving your choices.\nAll of these choices will be saved to config.json.\nYou can reinitialize these choices from the menu.\nUse responsibly.\n""")
        print("What browser do you use?")
        print("[0] Chrome")
        print("[1] Firefox")
        while True:
            choice=input('< ')
            if choice == '0':
                config["browser"]["chrome"]=True
                break
            elif choice == '1':
                config["browser"]["firefox"]=True
                break
            else:
                print('Unexpected choice.')
        
        print("What site do you want to nuke?")
        print("[0] Reddit")
        print("[1] Twitter")
        print("[2] both")
        while True:
            choice=input('< ')
            if choice == '0':
                config["sites"]["reddit"]=True
                break
            elif choice == '1':
                config["sites"]["twitter"]=True
                break
            elif choice == '2':
                config["sites"]["reddit"]=True
                config["sites"]["twitter"]=True
                break
            else:
                print('Unexpected choice.')
        
        print("What do you want to nuke?")
        print("[0] posts")
        print("[1] comments")
        print("[2] both")
        while True:
            choice=input('< ')
            if choice == '0':
                config["payload"]["posts"]=True
                break
            elif choice == '1':
                config["payload"]["comments"]=True
                break
            elif choice == '2':
                config["payload"]["posts"]=True
                config["payload"]["comments"]=True
                break
            else:
                print('Unexpected choice.')

        print('Saving choices...')
        config["init"]=False
        print("Choices saved!", end='\n') if core.write(path='config.json',arg='w',data=json.dumps(config)) else print('Choices not saved!', end='\n')
        print('Install the required driver.')
        open(driver.CHROME.value) if config["browser"]["chrome"]==True else open(driver.FIREFOX.value)

    while True:    
        print("<><><><><><><><><><><><><><><><>")
        print("[0] nuke")
        print("[1] show config")
        print("[2] open webdriver download page")
        print("[3] reinitialize choices")
        print("[-] exit",end="\n")
        choice=input('< ')
        if choice == '0':
            ...
        elif choice == '1':
            print(config)
        elif choice == '2':
            open(driver.CHROME.value) if config["browser"]["chrome"]==True else open(driver.FIREFOX.value)
        elif choice == '3':
            print("Choices reset!",end='\n') if core.write(path='config.json',arg='w',data=DEFAULT_CONFIG) else print('Choices not reset!', end='\n')
        elif choice == '-':
            exit()
        else:
            print('Unexpected input.')


        















