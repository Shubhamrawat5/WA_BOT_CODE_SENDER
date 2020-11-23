# WA_BOT_CODE_SENDER
Whatsapp bot to give programming codes

<hr>

## Command:-
### #gfg ProgramName

<hr> 

### example:-
### #gfg count set bits

```
// C++ program to Count set 
// bits in an integer 
#include <bits/stdc++.h> 
using namespace std; 
  
/* Function to get no of set bits in binary 
representation of positive integer n */
unsigned int countSetBits(unsigned int n) 
{ 
    unsigned int count = 0; 
    while (n) { 
        count += n & 1; 
        n >>= 1; 
    } 
    return count; 
} 
  
/* Program to test function countSetBits */
int main() 
{ 
    int i = 9; 
    cout << countSetBits(i); 
    return 0; 
} 
```

<hr>

## Install required libraries
pip install selenium

pip install requests

pip install bs4

pip install keyboard
<hr>

## Download web driver of your browser
[For chrome browser] https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_win32.zip 

Now set the PATH of this chrome web driver in environment variables (if did then comment line 7 and remove PATH from parameter in line 8

or edit the code, in line 7: PATH="paste here your chrome webdriver location"
<hr>

## READY TO USE!

#### Now run the WA_GFGcode_sender.py script, automatically new chrome will open and whatsapp web will get open, now scan the QR code !
#### chat will be loaded then click on a chat manually
#### now it will start scanning the last message of current chat and if it found a message start with #gfg then it will pick the message and search of whatever given after #gfg in google and then get first top link and then send request on that link and then does web scraping and extract the code result of the given program and then automatically write it in the message box and automatically send, if found! otherwise it will print "error!"
Also read code link 18
<hr>
