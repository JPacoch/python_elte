import time
from selenium import webdriver

refreshInterval = 16
viewsCount = 40
webpageLink = 'https://www.tiktok.com/@researchfund/video/6914260324837231878?lang=pl-PL'

driver = webdriver.Chrome('chromedriver.exe')
driver.get(webpageLink)

for i in range(viewsCount):
    time.sleep(refreshInterval)
    driver.refresh()
    print(i)   