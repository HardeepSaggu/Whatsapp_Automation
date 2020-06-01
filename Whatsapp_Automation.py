""" Requirements
	Chrome Driver same as installed chrome in operating system
"""



from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import socket

driver = webdriver.Chrome("E:/Whatsapp_Automation/chromedriver.exe")
driver.get('https://web.whatsapp.com/')
sleep(30)

message_text=["Message is this"]



def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com",80))
        return True
    except :
        is_connected()


def shift_enter(txt_box):
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
    txt_box.send_keys('\b')


def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for i in text:
            for t in i:
                if (t=='\n'):
                    shift_enter(txt_box)
                else:
                    txt_box.send_keys(t)
        txt_box.send_keys("\n")
    except Exception as e:
        print("Invalid phone no :"+str(phone_no))

l=[""]

for mobile_no in l:
    try:
        send_whatsapp_msg(mobile_no,message_text)
    except Exception as e:
        is_connected()


driver.close()
