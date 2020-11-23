import requests
from bs4 import BeautifulSoup as bs
import time
import keyboard

q='reverse a string' #program name

url='https://www.google.com/search?q='

response=requests.get(url+q+'+gfg') #searching for gfg links so adding gfg in query, also automatically + is added in place of space

soup=bs(response.content,"lxml")

desiredLink=soup.find("div",class_='kCrYT').a['href']  #get first top link

response=requests.get('https://www.google.com'+desiredLink)

soup=bs(response.content,"lxml")
inner=soup.find("div",class_='code-block')
container=inner.find("div",class_='container')
lines=container.findAll("div")
l=[]
for line in lines:
    txt=line.text
    txt=txt.replace(u'\xa0', u' ')
    print(txt)
    l.append(txt)

#print(l)
code="\n".join(l)
print(code)

# NOTE: using keyboard library to send the code text, uncomment below lines to send the code to post somewhere automatically
# time.sleep(2)
# for i in l:
#     #print(i)
#     keyboard.write(i)
#     keyboard.press_and_release('shift+enter')

# keyboard.press_and_release('enter') #send the message(code) written

#saving the code in a file name code.txt
# r=open(r'C:\Users\Shubham\Desktop\Program\code.txt','w',encoding='utf-8')
# r.write(code)
# print("Code saved in code.txt file locally!")
# r.close()
