from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.naver.com/')
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

print('Title:' + soup.title.string)
articles = soup.findAll('div', {'class' : 'u_skip'})
print(articles[0].txt)
