#import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import date, timedelta

#mail_usr='study.ai_172@mail.ru'
#password = 'NextPassword172#'

chrome_options = Options()
chrome_options.add_argument("start_maximized")

s = Service('./chromedriver.exe')
drv = webdriver.Chrome(service=s, options=chrome_options)
drv.get("https://account.mail.ru/")

input_usr = WebDriverWait(drv,5).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
input_usr.send_keys("study.ai_172@mail.ru")

drv.implicitly_wait(0.1)

btn = drv.find_element(By.XPATH,"//button[@data-test-id='next-button']")
btn.click()
drv.implicitly_wait(0.3)
input_pswd = WebDriverWait(drv,5).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
drv.implicitly_wait(0.3)
input_pswd.send_keys("NextPassword172#")


#drv.implicitly_wait(0.2)
btn = drv.find_element(By.XPATH,"//button[@data-test-id='submit-button']")
#drv.implicitly_wait(0.1)
btn.click()
drv.implicitly_wait(3)

mail_cnt_elem = WebDriverWait(drv,5).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class,'nav__item_active')]")))
#mails = WebDriverWait(drv, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'DtFVPxX_DtFVPKB')]")))
drv.implicitly_wait(0.1)
mail_link_set = set()
last_eleme = None
n=0
drv.implicitly_wait(1)
while mail_cnt_elem !=None and n<5:
    n=n+1
    #DtFVPxX_DtFVPKB
    mails = WebDriverWait(drv,5).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class,'llc')]")))
    #mails = WebDriverWait(drv, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'DtFVPxX_DtFVPKB')]")))
    mails_link =[]
    m=0
    for mail in mails:
        m=m+1
        mail_link=drv.get(mail.get_attribute('href'))
        #mail_link = mail.xpath("./@href")
        #mails_link.append(mail.get_attribute('href'))
    print(m)
print(n)




