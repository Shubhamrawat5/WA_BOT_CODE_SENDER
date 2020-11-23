import requests
from bs4 import BeautifulSoup as bs
import keyboard
from selenium import webdriver
import time

PATH="C:\\Users\\Shubham\\Downloads\\chromedriver_win32\\chromedriver.exe" #path of chrome webdriver [edit your path]
driver=webdriver.Chrome(PATH)

time.sleep(2)

url="https://web.whatsapp.com/"
driver.get(url)

input("WAIT TILL SCAN QR CODE OF WHATSAPP COMPLETE THEN PRESS ENTER!")

input("NOW OPEN A WHATSAPP CHAT AND PRESS ENTER")
#if you want to automatically open a particular chat, then uncomment below two lines and change the title to the chat of your!
#group=driver.find_element_by_css_selector('span[title="Bot test"]')
#group.click()


def refresh():
    time.sleep(1)

    #total chats in current chat
    chats=driver.find_elements_by_class_name('_1wlJG') #this class name is of messages in chat. all messsages comes under same class, also this class is changed by WA time to time i think so if you got error like "out of index" then change this class name

    #get last message in total chat
    try:
        msg=chats[-1].text
        print("Message is:"+msg)
    except:
        print("Either chat is empty or messages class name has changed, check link 27 in code")

    try:
        if msg[0:4]=='#gfg': # query asked!
            q=msg[5:]
            print("QUERY FOUND !\nProgram to be search is "+q)

            url='https://www.google.com/search?q='

            response=requests.get(url+q+'+gfg')

            soup=bs(response.content,"lxml")

            desiredLink=soup.find("div",class_='kCrYT').a['href']

            g='https://www.google.com'

            response=requests.get('https://www.google.com'+desiredLink)

            #xpath='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]' #path of the typing box of whatsapp chat
            #msgbox=driver.find_element_by_xpath(xpath)

            soup=bs(response.content,"lxml")
            code=soup.find("div",class_='code-block').text
            code=code.replace(u'\xa0', u' ')
            code=code[79:]

            time.sleep(2)

            for i in code:
                #print(i)
                if i != '\n':
                    keyboard.write(i)
                else:
                    keyboard.press_and_release('shift+enter')

            keyboard.press_and_release('enter')

            #print(code)
            time.sleep(2)
    except:
        print("ERROR")


time.sleep(4)
while True:
    print("-----SCANNING MESSAGES!!!-----")
    refresh()
    time.sleep(3)