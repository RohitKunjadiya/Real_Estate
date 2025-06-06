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

# price=max 30 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMax=30-Lacs&cityName=ahmedabad')
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
# with open('ahmedabad-1.html', 'w', encoding='utf-8') as f:
#     f.write(html)

# ----------------------------------------------------------------------------------------------------------------------

# price=30-40 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=30-Lacs&BudgetMax=40-Lacs&cityName=ahmedabad')
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
# with open('ahmedabad-2.html', 'w', encoding='utf-8') as f:
#     f.write(html)


# ----------------------------------------------------------------------------------------------------------------------

# # price=40-45 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=40-Lacs&BudgetMax=45-Lacs&cityName=ahmedabad')
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
# with open('ahmedabad-3.html', 'w', encoding='utf-8') as f:
#     f.write(html)


# ----------------------------------------------------------------------------------------------------------------------

# price=45-50 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=45-Lacs&BudgetMax=50-Lacs&cityName=ahmedabad')
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
# with open('ahmedabad-4.html', 'w', encoding='utf-8') as f:
#     f.write(html)

# ----------------------------------------------------------------------------------------------------------------------

# price=50-56 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=50-Lacs&BudgetMax=56-Lacs&cityName=ahmedabad')
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
# with open('ahmedabad-5.html', 'w', encoding='utf-8') as f:
#     f.write(html)


# ----------------------------------------------------------------------------------------------------------------------

# price=57-63 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=57-Lacs&BudgetMax=63-Lacs&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<50:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
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
# with open('ahmedabad-6.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# ----------------------------------------------------------------------------------------------------------------------

# price=64-69 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=64-Lacs&BudgetMax=69-Lacs&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<40:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-7.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# ----------------------------------------------------------------------------------------------------------------------

# price=70-75 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=70-Lacs&BudgetMax=75-Lacs&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<35:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-8.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# ----------------------------------------------------------------------------------------------------------------------

# price=76-85 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=76-Lacs&BudgetMax=85-Lacs&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<50:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-9.html', 'w', encoding='utf-8') as f:
#     f.write(html)


# ----------------------------------------------------------------------------------------------------------------------

# price=86-100 lacs flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=86-Lacs&BudgetMax=1-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<41:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-10.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# ----------------------------------------------------------------------------------------------------------------------

# price = 1 - 1.2 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=1-Crore&BudgetMax=1.2-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<47:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-11.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# ----------------------------------------------------------------------------------------------------------------------

# price = 1.2 - 1.4 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=1.2-Crore&BudgetMax=1.4-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<56:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-12.html', 'w', encoding='utf-8') as f:
#     f.write(html)


# # ----------------------------------------------------------------------------------------------------------------------
#
# # price = 1.4 - 1.6 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=1.4-Crore&BudgetMax=1.6-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<56:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-13.html', 'w', encoding='utf-8') as f:
#     f.write(html)
#
#
# # ----------------------------------------------------------------------------------------------------------------------
#
# # price = 1.6 - 2 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=1.6-Crore&BudgetMax=2-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<56:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-14.html', 'w', encoding='utf-8') as f:
#     f.write(html)

#
# # ----------------------------------------------------------------------------------------------------------------------
#
# # price = 2 - 2.6 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=2-Crore&BudgetMax=2.6-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<56:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-15.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# # ----------------------------------------------------------------------------------------------------------------------
#
# # price = 2.6 - 3.5 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=2.6-Crore&BudgetMax=3.5-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<56:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-16.html', 'w', encoding='utf-8') as f:
#     f.write(html)
#
# # ----------------------------------------------------------------------------------------------------------------------
#
# # price = 3.5 - 4.5 crore flats ahmedabad
# driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=3.5-Crore&BudgetMax=4.5-Crore&cityName=ahmedabad')
# time.sleep(2)
#
# old_height = driver.execute_script("return document.body.scrollHeight")
#
# counter = 1
# while counter<45:
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
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
# with open('ahmedabad-17.html', 'w', encoding='utf-8') as f:
#     f.write(html)



# ----------------------------------------------------------------------------------------------------------------------

# price = 4.5 - max crore flats ahmedabad
driver.get('https://www.magicbricks.com/property-for-sale/residential-commercial-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&BudgetMin=4.5-Crore&BudgetMax=max&cityName=ahmedabad')
time.sleep(2)

old_height = driver.execute_script("return document.body.scrollHeight")

counter = 1
while counter<54:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(counter)
    counter += 1
    print(old_height,new_height)

    if new_height == old_height:
        continue
    old_height = new_height

html = driver.page_source

with open('ahmedabad-18.html', 'w', encoding='utf-8') as f:
    f.write(html)