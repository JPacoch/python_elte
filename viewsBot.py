import time
from selenium import webdriver

refreshInterval = 1
viewsCount = 20
webpageLink = 'https://twitter.com/JakubPacocha'

driver = webdriver.Chrome('chromedriver.exe')
driver.get(webpageLink)

for i in range(viewsCount):
    time.sleep(refreshInterval)
    driver.refresh()
    print(i)