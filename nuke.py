import json
from enum import Enum
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

import core

BANNER:str=r"""
 ________  ________  ________  ___  ________  ___               ________   ___  ___  ___  __    _______      
|\   ____\|\   __  \|\   ____\|\  \|\   __  \|\  \             |\   ___  \|\  \|\  \|\  \|\  \ |\  ___ \     
\ \  \___|\ \  \|\  \ \  \___|\ \  \ \  \|\  \ \  \            \ \  \\ \  \ \  \\\  \ \  \/  /|\ \   __/|    
 \ \_____  \ \  \\\  \ \  \    \ \  \ \   __  \ \  \            \ \  \\ \  \ \  \\\  \ \   ___  \ \  \_|/__  
  \|____|\  \ \  \\\  \ \  \____\ \  \ \  \ \  \ \  \____        \ \  \\ \  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
    ____\_\  \ \_______\ \_______\ \__\ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\\ \__\ \_______\
   |\_________\|_______|\|_______|\|__|\|__|\|__|\|_______|        \|__| \|__|\|_______|\|__| \|__|\|_______|
   \|_________|                                                                                     by valtyr
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""

DEFAULT_CONFIG:str='{"init": true, "sites": {"reddit": false, "twitter": false}, "payload": {"posts": false, "comments": false}}'

class sites(Enum):
    REDDIT:str = "https://www.reddit.com"
    TWITTER:str = "https://twitter.com/home"

class payloads(Enum):
    POSTS:str = "POSTS"
    COMMENTS:str = "COMMENTS"

def nuke_reddit():
    ...
    #the webdriver steps

def nuke_twitter():
    ...
    #the webdriver steps

if __name__=="__main__":
    print(BANNER)

    config = json.loads(core.read(path="config.json",arg="r"))

    if config['init'] == True:
        print("""Looks like this is your first time using this tool...\nSo here's how it works.\n\t- Select which sites you want to nuke.\n\t- Select what you want to nuke.\nAll of these choices will be saved to config.json.\nYou can reinitialize these choices from the menu.\nUse responsibly.\n""")
         
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

    while True: 
        nuking:bool=False   
        print("[0] nuke")
        print("[1] show config")
        print("[2] reinitialize choices")
        print("[-] exit",end="\n")
        choice=input('< ')
        if choice == '0':

            #TODO DISPLAY OPTIONS AND CONFIRM NUKE
            
            #Maybe add firefox in future
            # if config['browser']['chrome'] == True else webdriver.Firefox(executable_path="F:/valtyr/nuke/drivers/geckodriver.exe")

            #DRIVE SEPERATE INSTANCES
            #TODO get full path from os

            print("Nuking...")
            nuking=True

            if config['sites']['reddit'] == True:
                driver_reddit = webdriver.Chrome("F:/valtyr/nuke/drivers/chromedriver.exe") 
                driver_reddit.get(sites.REDDIT.value) 
            if config['sites']['twitter'] == True:
                driver_twitter = webdriver.Chrome("F:/valtyr/nuke/drivers/chromedriver.exe") 
                driver_twitter.get(sites.TWITTER.value) 

                #NUKE HERE
           
        elif choice == '1':
            print(config)
        elif choice == '2':
            core.write(path='config.json',arg='w',data=DEFAULT_CONFIG)
            print('Choices reset!')
            print('Restart required.')
            exit()
        elif choice == '-':
            exit()
        else:
            print('Unexpected input.')

        if nuking:
            break


        















