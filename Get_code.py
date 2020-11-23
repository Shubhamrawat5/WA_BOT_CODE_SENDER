import requests
from bs4 import BeautifulSoup as bs
import time
import keyboard

q='count set bits' #program name

url='https://www.google.com/search?q='

response=requests.get(url+q+'+gfg') #searching for gfg links so adding gfg in query, also automatically + is added in place of space

soup=bs(response.content,"lxml")

desiredLink=soup.find("div",class_='kCrYT').a['href']  #get first top link

response=requests.get('https://www.google.com'+desiredLink)

soup=bs(response.content,"lxml")
code=soup.find("div",class_='code-block').text #get code in gfg page
code=code.replace(u'\xa0', u' ') #there are many \x0 in code so replacing all with space
code=code[79:] #slicing unnecessary part in front

# NOTE: using keyboard library to send the code text, uncomment below lines to send the code to post somewhere automatically
# time.sleep(2)
# for i in code:
#     #print(i)
#     if i != '\n': #\n is treated as enter, so if \n come then it will instead of breaking link, it will send the message.. so handling it here
#         keyboard.write(i)
#     else:
#         keyboard.press_and_release('shift+enter')

# keyboard.press_and_release('enter') #send the message(code) written

print(code)

#saving the code in a file name code.txt
r=open(r'C:\Users\Shubham\Desktop\Program\code.txt','w',encoding='utf-8')
r.write(code)
print("Code saved in code.txt file locally!")
r.close()
