# -*- coding: utf-8 -*-
"""EXNO-2-APPDS-GB.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X0E4hCwiZEi8URRiSiw2CtYMSqUTzu6w
"""

pip install requests beautifulsoup4 pandas selenium

import requests
url = 'https://www.w3schools.com/html/html_tables.asp'
response = requests.get(url)
html_content = response.text

html_content

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')



!pip install selenium
!apt-get update
!apt install chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options to run in headless mode
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

url = 'https://www.geeksforgeeks.org/python-programming-language-tutorial/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting article titles

# Saving to CSV