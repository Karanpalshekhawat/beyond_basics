from bs4 import BeautifulSoup
import requests
import csv

"""This will be an html output"""
source = requests.get("https://coreyms.com").text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p. text

print(summary)