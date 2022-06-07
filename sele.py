#Automated morse code sender through morse chat interface 
from selenium import webdriver
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
browser.get('http://morsecode.me/?room=2')
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div")))

def encrypt(message): 
    cipher = '' 
    for letter in message :
            if letter != ' ' and letter in MORSE_CODE_DICT:
                cipher += MORSE_CODE_DICT[letter] + ' '
            else: 
                cipher += ' '
    return cipher 

def decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0   # counter to keep track of space 
            citext += letter # storing morse code of a single character 
       
        else:                                         # in case of space 
            i += 1                                  # if i = 1 that indicates a new character 
            if i == 2 :                             # if i = 2 that indicates a new word 
                decipher += ' '                # adding space to separate words 
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT   # accessing the keys using their values (reverse of encryption) 
                .values()).index(citext)] 
                citext = '' 

    return decipher 

shortT = 0.08  
longT = 0.2

def send_morse(complete_message):
    for message in complete_message:
        for char in message:
            if message == "." :
                ActionChains(browser).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.02)   
            elif message == "-" :                               # LONG PRESS
                ActionChains(browser).key_down(Keys.SPACE).perform()
                time.sleep(longT)
                ActionChains(browser).key_up(Keys.SPACE).perform()
                time.sleep(0.02)   
            elif message == "*":
                time.sleep(longT+0.2)
                                  

def main():
    try:
        message = "int err upt"
        result = encrypt(message.upper())
        message = result.replace(" ", "*")
        testMessage = message.split()

        while True:
            for msg in testMessage:
                send_morse(msg)
                time.sleep(longT+0.12)
            
            message = input("enter your message: ")
            result = encrypt(message.upper()) 
            message = result.replace(" ", "*")  
            testMessage = message.split()

    except KeyboardInterrupt :
        print('Interrupted')
        browser.quit()

if __name__ == "__main__":
    main()
     