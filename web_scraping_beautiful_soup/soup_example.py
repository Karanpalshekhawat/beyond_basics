"""
Although we pip install beautifulsoup4 but it is imported like below
"""
from bs4 import BeautifulSoup


with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

match = soup.title
print(match.text)

match2 = soup.find('div')
print(match2)

# different div with class information
print(soup.find('div', class_='footer'))

article = soup.find('div', class_='article')
headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
print()

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()
