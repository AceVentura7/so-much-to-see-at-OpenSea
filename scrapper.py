!pip install kora -q
from kora.selenium import wd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import smtplib
import os

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver
driver=get_driver()

def get_nft_title():
  nft_div_tag='Rankings_tableRowLink__2wVPO'
  driver.get(flip_url)
  time.sleep(5)
  nft=driver.find_elements(By.CLASS_NAME,nft_div_tag)
  nft_title=[]
  for i in nft:
    nft_title.append(i.text)
  return nft_title

def get_nft_vol():
  ranks=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[4]')
  nft_vol=[]
  for i in ranks:
    #print(i.text)
    nft_vol.append(i.text)
  return nft_vol

def get_nft_sales():
  sale=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[5]')
  nft_sale=[]
  for i in sale:
    #print(i.text)
    nft_sale.append(i.text)
  return nft_sale

def nft_floor_price():
  fl_price=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[6]')
  nft_fl_price=[]
  for i in fl_price:
    #print(i.text)
    nft_fl_price.append(i.text)
  return nft_fl_price

def get_nft_change():
  fl_change=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[7]')
  nft_fl_change=[]
  for i in fl_change:
    #print(i.text)
    nft_fl_change.append(i.text)
  return nft_fl_change

def get_nft_owners():
  owners=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[8]')
  nft_owners=[]
  for i in owners:
    #print(i.text)
    nft_owners.append(i.text)
  return nft_owners

def get_nft_owners_change():
  own_change=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[9]')
  nft_own_change=[]
  for i in own_change:
    #print(i.text)
    nft_own_change.append(i.text)
  return nft_own_change

def nft_supply_listed():
  listed_suppy=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[10]')
  nft_supply_listed=[]
  for i in listed_suppy:
    #print(i.text)
    nft_supply_listed.append(i.text)
  return nft_supply_listed
  
def get_nft_listings():
  listings=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[11]')
  nft_listings=[]
  for i in listings:
    #print(i.text)
    nft_listings.append(i.text)
  return nft_listings

def scrape_nft():
    nft_url = 'https://www.flips.finance/'
    driver=get_driver()
    nft_dict = {
        'Title': get_nft_title(),
        'Volume': get_nft_vol(),
        'Sales': get_nft_sales(),
        'Floor Price': nft_floor_price(),
        '24 hr Change': get_nft_change(),
        'Total Ownsers': get_nft_owners(),
        'Change Owners': get_nft_owners_change(),
        '% Supply Listed': nft_supply_listed(),
        '24 hr Listing Change': get_nft_listings(),
        #'Image_url': get_nft_img()
    }
    return pd.DataFrame(nft_dict)

scrape_nft()