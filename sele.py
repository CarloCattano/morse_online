'''Automated morse code sender through morse chat interface 
'''
from selenium import webdriver
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ',':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-','!' : '---.',
    ':': '---...',"'" : '.----.','@' : '.--.-.',
    '=' : '-...-'
}

browser = webdriver.Firefox()
browser.get('http://morsecode.me/?room=1')

button = browser.find_element_by_id("key")

action_key_down_w = ActionChains(browser).key_down(Keys.RETURN)
action_key_up_w = ActionChains(browser).key_up(Keys.RETURN)

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
  
    return cipher 
  
def decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        # checks for space 
        if (letter != ' '): 
            # counter to keep track of space 
            i = 0
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
    return decipher 
  
shortT = 0.08               # 80 ms
longT = 0.3                # 100ms
spaceT = 0.4

message = "Hello  Im greta tuneberg" # text we convert to morse code
result = encrypt(message.upper()) 
print("Text encripted to morse : ",result)

message = result.replace(" ", "*")

testMessage = message.split()

print("splitted ",testMessage)

def send_morse(complete_message):
    for message in complete_message:
        for char in message:

            if message == "." :
                
                action_key_down_w.perform()  #keydown press
                action_key_up_w.perform()
               

            elif message == "-" :  # LONG PRESS
                action_key_down_w.perform()
                time.sleep(longT)
                action_key_up_w.perform()

            elif message == "*":
                time.sleep(longT)    

        time.sleep(0.05) #time between letters    

try:
    while True:
        time.sleep(0.5)
        for msg in testMessage:
            send_morse(msg)
            print("sending now " ,msg)
            time.sleep(spaceT)
        time.sleep(0.5)

        print("-")
        print("--") 
        print("Message transmission completed")
        print("--")
        print("-") 

        message = input("enter your message: ")   
        result = encrypt(message.upper()) 
        print("Text encoded into morse : ",result)
        message = result.replace(" ", "*")
        testMessage = message.split()

except KeyboardInterrupt :
    print('Interrupted')
    browser.quit()

     