from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://web.whatsapp.com/')
time.sleep(25)

string1 = 'This message is sent using python for Priyansh'
string2 = 'This message is sent using python for Jayraj'
string = 'Offline'

#xtarget = driver.find_element_by_class_name('TbtXF')
#time.sleep(2)
#xtarget.click()

input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]')
for i in range(399):
    time.sleep(0.13)
    input_box.send_keys(string, Keys.ENTER)
