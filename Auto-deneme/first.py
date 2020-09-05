from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.maximize_window()
chrome_browser.get("https://google.com")
sleep(10)
chrome_browser.get("https://duckduckgo.com")
