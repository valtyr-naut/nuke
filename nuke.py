from selenium.webdriver.common.keys import Keys as keys
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

class site(Enum):
    WEBPAGE_REDDIT:str = "https://www.reddit.com"
    WEBPAGE_TWITTER:str = "https://twitter.com/home"

class driver(Enum):
    CHROME:str = "https://chromedriver.chromium.org/downloads"
    FIREFOX:str = "https://github.com/mozilla/geckodriver/releases"

class payload(Enum):
    ALL:str = "ALL"
    POSTS:str = "POSTS"
    COMMENTS:str = "COMMENTS"






if __name__=="__main__":
    print(BANNER)
    print(core.read(path="persistence.json",arg="r"))














