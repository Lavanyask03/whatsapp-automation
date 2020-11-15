#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
# add your chromedriver.exe file path
browser = webdriver.Chrome("C:/Users/Lavanya.DESKTOP-SIIUMJV/chromedriver_win32/chromedriver.exe")
browser.get("https://www.selenium.dev/")
search = browser.find_element_by_id("gsc-i-id1")
search.send_keys("Downloads")


# In[13]:


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

# add your chromedriver.exe file path
driver = webdriver.Chrome("C:/Users/Lavanya.DESKTOP-SIIUMJV/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)

receiver = str(input("Enter the recipient name: "))
target = "'" + receiver + "'"

print("1.Message")
print("2.Image")
n = int(input())

x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()

if n==1:
    message = input("Enter the message: ")
    input_box = driver.find_element_by_class_name("_3uMse")
    input_box.send_keys(message+Keys.ENTER)
    print("Message sent to",receiver)
    
elif n==2:
    filepath = input("Enter the file path: ")
    attachment = driver.find_element_by_xpath('//div[@title="Attach"]')
    attachment.click()

    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    sleep(3)

    send_btn = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_btn.click()
    print("Image sent to",receiver)





