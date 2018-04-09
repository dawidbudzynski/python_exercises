# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
# New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
all_h2 = soup.find_all(class_='story-heading')
counter = 0

for item in all_h2:
    try:
        print('Article no: {} - {}'.format(counter, item.a.text.strip('\n').strip('            ')))
        counter += 1
    except AttributeError:
        print('Article no: {} - {}'.format(counter, item.contents[0].strip()))
        counter += 1

# done
