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

flip_url = 'https://www.flips.finance/'

# Function to get ALL NFT titles on the page

def get_nft_title():
  nft_div_tag='Rankings_tableRowLink__2wVPO'
  driver.get(flip_url)
  time.sleep(5)
  nft=driver.find_elements(By.CLASS_NAME,nft_div_tag)
  nft_title=[]
  for i in nft:
    nft_title.append(i.text)
  return nft_title

# Function to get ALL NFT volumes on the page

def get_nft_vol():
  ranks=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[4]')
  nft_vol=[]
  for i in ranks:
    #print(i.text)
    nft_vol.append(i.text)
  return nft_vol


# Function to get ALL NFT sales on the page

def get_nft_sales():
  sale=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[5]')
  nft_sale=[]
  for i in sale:
    #print(i.text)
    nft_sale.append(i.text)
  return nft_sale

# Function to get ALL NFT Floor Price on the page

def nft_floor_price():
  fl_price=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[6]')
  nft_fl_price=[]
  for i in fl_price:
    #print(i.text)
    nft_fl_price.append(i.text)
  return nft_fl_price


# Function to get ALL NFT % change on the page

def get_nft_change():
  fl_change=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[7]')
  nft_fl_change=[]
  for i in fl_change:
    #print(i.text)
    nft_fl_change.append(i.text)
  return nft_fl_change


# Function to get ALL NFT Owners on the page

def get_nft_owners():
  owners=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[8]')
  nft_owners=[]
  for i in owners:
    #print(i.text)
    nft_owners.append(i.text)
  return nft_owners


# Function to get ALL % NFT Owners Chnage on the page

def get_nft_owners_change():
  own_change=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[9]')
  nft_own_change=[]
  for i in own_change:
    #print(i.text)
    nft_own_change.append(i.text)
  return nft_own_change


# Function to get ALL NFT Suppy Listed on the page

def nft_supply_listed():
  listed_suppy=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[10]')
  nft_supply_listed=[]
  for i in listed_suppy:
    #print(i.text)
    nft_supply_listed.append(i.text)
  return nft_supply_listed


# Function to get ALL NFT % Listings on the page

def get_nft_listings():
  listings=driver.find_elements(By.XPATH, '//tr[@class="Rankings_rankTableRow__1SwSX"]/td[11]')
  nft_listings=[]
  for i in listings:
    #print(i.text)
    nft_listings.append(i.text)
  return nft_listings

#We are only going to scrape all the top NFTs on the page.

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
        #'Other Links' : get_other_links()
                
    }
    return pd.DataFrame(nft_dict)

df = scrape_nft()

# saving the DataFrame as a CSV file
nft_csv_data = df.to_csv('NFT.csv', index = False)
print('\nCSV String:\n', nft_csv_data)



# Function to get links from 2nd page for each of the NFT's. Due to time constraints using (.sleep) we shall only do 10.

driver.get('https://www.flips.finance/') #issue


def get_other_links():
  final_list=[]
  for i in range(10):
    driver.get('https://www.flips.finance/')
    time.sleep(3)
    y=get_driver().find_elements(By.CLASS_NAME,'Rankings_tableRowLink__2wVPO')
    #print(y[i])
    x=y[i]
    x.click()
    time.sleep(5)
    z=get_driver().find_elements(By.CLASS_NAME,'cstats_l__6AaiS')
    #nft_links.append(z.get_attribute('href'))
    nft_links = []
    for j in z:
      p=j.get_attribute('href')
      nft_links.append(p)
    final_list.append(nft_links)
  return final_list

other_links = get_other_links()

#We are only going to scrape the top 10 NFTs on the page and get the links available on the same 10 pages to create another csv file.

def scrape_nft2():
    nft_url = 'https://www.flips.finance/'
    driver=get_driver()
    nft_dict2 = {
        'Title': get_nft_title()[:10],
        'Volume': get_nft_vol()[:10],
        'Sales': get_nft_sales()[:10],
        'Floor Price': nft_floor_price()[:10],
        '24 hr Change': get_nft_change()[:10],
        'Total Ownsers': get_nft_owners()[:10],
        'Change Owners': get_nft_owners_change()[:10],
        '% Supply Listed': nft_supply_listed()[:10],
        '24 hr Listing Change': get_nft_listings()[:10],
        'Other Links' : get_other_links()
                
    }
    return pd.DataFrame(nft_dict2)

df_2 = scrape_nft2()

# saving the DataFrame as a CSV file
nft_csv_data = df_2.to_csv('NFT(10).csv', index = False)
print('\nCSV String:\n', nft_csv_data)

# send email code, somethings off with this aswell @samanvita

'''
def send_email():
  
  try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()

    sender_email = 'sendtrends7@gmail.com'
    receiver_email = 'sendtrends7@gmail.com'  
    my_secret = os.environ['gmail_pass']
    print('Password:', my_secret)
    subject = 'OMG Test Message from Replit'
    body = 'Hey, this is a test email sent via replit using python'
    
    email_text = f"""
    From: {sender_email}
    To: {receiver_email}
    
    Subject: {subject}
    
    {body}
    """
    server_ssl.login(sender_email, my_secret)
    server_ssl.sendmail(sender_email, receiver_email, email_text)
    server_ssl.close()
    
  except:
    print ('Something went wrong...')

send_email()
'''

