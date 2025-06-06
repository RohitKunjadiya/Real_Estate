import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

s = Service('C://Users//praye//OneDrive//Desktop//chromedriver-win64//chromedriver-win64//chromedriver.exe')

chrome_options = Options()
chrome_options.add_experimental_option(name="detach",value=True)
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(service=s, options=chrome_options)
#
# # price=max 60 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMax=60-Lacs&cityName=surat')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<70:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(4)
#
#     new_height = driver.execute_script("return document.body.scrollHeight")
#
#     print(counter)
#     counter += 1
#     print(old_height,new_height)
#
#     if new_height == old_height:
#         continue
#     old_height = new_height
#
# html = driver.page_source
#
#
# with open('surat-1.html', 'w', encoding='utf-8') as f:
#     f.write(html)

# ----------------------------------------------------------------------------------------------------------------------


# # price=60 lacs - 1.6cr flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=60-Lacs&BudgetMax=1.6-Crore&cityName=surat')
# time.sleep(3)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<65:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(4)
#
#     new_height = driver.execute_script("return document.body.scrollHeight")
#
#     print(counter)
#     counter += 1
#     print(old_height,new_height)
#
#     if new_height == old_height:
#         continue
#     old_height = new_height
#
# html = driver.page_source
#
#
# with open('surat-2.html', 'w', encoding='utf-8') as f:
#     f.write(html)
# ----------------------------------------------------------------------------------------------------------------------

# price= 1.6cr - max flats ahmedabad
driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=1.6-Crore&BudgetMax=20-Crore&cityName=surat')
time.sleep(3)

old_height = driver.execute_script("return document.body.scrollHeight")

counter = 1
while counter<70:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(counter)
    counter += 1
    print(old_height,new_height)

    if new_height == old_height:
        continue
    old_height = new_height

html = driver.page_source


with open('surat-3.html', 'w', encoding='utf-8') as f:
    f.write(html)

