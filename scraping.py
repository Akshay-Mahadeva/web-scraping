from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

# URL of the website to take data from
URL = ''

# Get headers from a specific link (Find Your User-Agent: https://httpbin.org/get)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

page = requests.get(URL, headers = headers)