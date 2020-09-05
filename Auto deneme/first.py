from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.maximize_window()
chrome_browser.get("https://google.com")
WebDriverWait(chrome_browser, timeout=10)
chrome_browser.get("https://duckduckgo.com")
