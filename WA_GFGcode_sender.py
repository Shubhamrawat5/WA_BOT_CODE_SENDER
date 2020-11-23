import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys #for keyboard keys pressing like for next line = shift+enter
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

    #Find class name of message
    try:
        outer=driver.find_element_by_css_selector('div[class="copyable-text"]')
        inner=outer.find_element_by_css_selector('div[dir="ltr"]')
        msg_class=inner.get_attribute("class")
    except:
        try:
            outer=driver.find_element_by_css_selector('div[class="cln10 copyable-text"]')
            inner=outer.find_element_by_css_selector('div[dir="ltr"]')
            msg_class=inner.get_attribute("class")
        except:
            print("Error in classname!!!!")
            exit()

    try:
        #total chats in current chat
        chats=driver.find_elements_by_class_name(msg_class)

        #get last message in total chat
        msg=chats[-1].text
        print("Message is:"+msg)
    except:
        print("Either chat is empty or messages class name is incorrect !")
        exit()

    try:
        if msg[0:4]=='#gfg': # query asked!
            q=msg[5:] 
            print("QUERY FOUND !\nProgram to be search is "+q)

            url='https://www.google.com/search?q='

            response=requests.get(url+q+'+gfg') #searching in google

            soup=bs(response.content,"lxml")

            desiredLink=soup.find("div",class_='kCrYT').a['href'] #get first top link, gfg link it would be!

            g='https://www.google.com'

            response=requests.get('https://www.google.com'+desiredLink) #open link of gfg

            #scraping asked program code
            soup=bs(response.content,"lxml")
            inner=soup.find("div",class_='code-block')
            cont=inner.find("div",class_='container')
            lines=cont.findAll("div")

            #a list is creating of all the lines of program code
            l=[]
            for line in lines:
                txt=line.text
                txt=txt.replace(u'\xa0', u' ')
                #print(txt)
                l.append(txt)

            xpath='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]' #path of the typing box of whatsapp chat
            msgbox=driver.find_element_by_xpath(xpath)

            #now sending the program code to message box of whatsapp automatically
            for line in l:
                if line=='':
                    continue
                msgbox.send_keys(line)
                msgbox.send_keys(Keys.SHIFT+Keys.ENTER)

            msgbox.send_keys(Keys.ENTER)
            print("-------------------\n PROGRAM SENT SUCCESSFULLY ! \n-------------------")
    except:
        print("ERROR IN GETTING PROGRAM !")


time.sleep(4)
while True:
    print("-----SCANNING MESSAGES!!!-----")
    refresh()
    time.sleep(2)