from selenium import webdriver
from bs4 import BeautifulSoup
import time

URL = "https://helloworldcollection.de/"
browser = webdriver.Chrome(executable_path="path_to_chromedriver.exe")
sada = browser.get(URL)
time.sleep(3)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

file = open("words.txt", 'w')
for items in soup.find_all('pre'):
    file.write(items.text)
    print(items.text)