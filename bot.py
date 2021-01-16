from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os
 

print("What do you want to download?")
download = input()
path="./dataset/"+download
os.mkdir(path)
n=int(input("Number of images \n"))
site = 'https://www.google.com/search?tbm=isch&q='+download


driver = webdriver.Firefox(executable_path = 'C:\Drivers\geckodriver.exe')
driver.get(site)

i = 0

while i< int(n/8):  
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    
    try:
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(5)
    i+=1

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()
img_tags = soup.find_all("img", class_="rg_i",limit = n)


count = 0
for i in img_tags:
    try:
        urllib.request.urlretrieve(i['src'],path+'/'+str(count)+".jpg")
        count+=1
        print("Number of images downloaded = "+str(count),end='\r')
    except Exception as e:
        pass
