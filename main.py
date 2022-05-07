#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Dennys Augustus / dennysaug@gmail.com
# python main.py

#dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_90.0.4430.93-1 _amd64.deb
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# sudo apt-get install python-mysqldb
# sudo apt-get install chromedriver
# pip install selenium==3.12
# pip install requests==2.19.1


import os
import requests
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException


def main():

    pastaAtual = os.getcwd()

    auction_url = "https://play.alienworlds.io/inventory"

    print("Starting...")

    # C:\Users\Dennys Oliveira\AppData\Local\Google\Chrome\User Data

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/home/dennys/.config/google-chrome")
    # options.add_argument("--user-data-dir="+pastaAtual+"/google-chrome")
    options.add_argument("disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1420,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--single-process')

    chromedriver = pastaAtual + "/chromedriver"
    # chromedriver = '/usr/lib/chromium/chromedriver'
    # chromedriver = '/usr/src/app/driver/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver

    while True:

        if check_internet(auction_url):

            browser = webdriver.Chrome(options=options, executable_path=chromedriver)
            browser.maximize_window()
            browser.get(auction_url)
            print("Opening website play.alienworlds.io\n")

            sleep(4)
            print("Clicking on Start Now\n")
            try:
                browser.find_element_by_xpath("//*[contains(text(), 'Start Now')]").click()
            except (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException) as e:
                pass

            print("Waiting 15s")
            sleep(15)
            loop = 0
            while True:

                loop += 1

                print(str(loop) + " Loop")

                print("Clicking on Mine")

                intCount = 0
                while True:

                    try:
                        browser.find_element_by_xpath("//*[contains(text(), 'Mine')]").click()
                        sleep(1)
                        break
                    except (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException) as e:
                        intCount = intCount + 1
                        sleep(3)

                sleep(10)
                print("Clicking on Claim Mine")
                intCount = 0
                while True:

                    try:
                        browser.find_element_by_xpath("//*[contains(text(), 'Claim Mine')]").click()
                        sleep(1)
                        break
                    except (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException) as e:
                        intCount += 1
                        sleep(3)

                sleep(15)
                print("Changing to pop-up")
                browser.switch_to.window(browser.window_handles[1])
                print("Aprroving")
                intCount = 0
                while True:

                    try:
                        browser.find_element_by_xpath("//*[contains(text(), 'Approve')]").click()
                        sleep(1)
                        break
                    except (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException) as e:
                        intCount += 1
                        sleep(3)

                print("Back to main page")
                browser.switch_to.window(browser.window_handles[0])
                print("Let's mining!\n\n")
                sleep(420)
                sleep(10)


                if loop % 10 == 0:
                    print('sleeping 30min')
                    sleep(1800) #1hr


def check_internet(url='http://www.google.com/', timeout=1, hm=''):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.exceptions.ReadTimeout):
        print("[*] No connection")
        return False

if __name__ == '__main__':
    main()

# fim
