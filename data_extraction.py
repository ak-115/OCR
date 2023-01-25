from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import win32clipboard
import time
import os
from colorama import Fore

data = ''
def cp():
    global data
    win32clipboard.OpenClipboard()
    data1 = win32clipboard.GetClipboardData()
    data += data1
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    print( Fore.YELLOW + data1)

def save():
    if inp == 'y':
        file = input(Fore.GREEN + 'Name of Output file: ')
        if file in os.listdir():
            os.remove(file)
            save()
        else:
            file = open(file, 'w', encoding='utf-8')
            with file:
                file.write(data)
    else:
        exit()


options = Options()
# options.headless = True
options.add_argument('--headless=new')

browser = webdriver.Chrome(options=options)
print(Fore.YELLOW)
browser.get('https://www.imagetotext.info/')

upload = browser.find_element(by='id', value='file')
img = input(Fore.GREEN +'Enter image path: ')
upload.send_keys(img)
submit = browser.find_element(by='id', value='jsShadowRoot')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
submit.click()
copy = browser.find_element(By.XPATH, '/html/body/section[1]/div/div/span[2]/span/div[1]/div/div[3]/button[1]')
time.sleep(15)
copy.click()


try:
    cp()
except Exception as e:
    print(Fore.RED + str(e))
    print("Trying again")
    cp()

inp = input(Fore.GREEN + 'Save output?(y/n)')
save()

