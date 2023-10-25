import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

pays_et_capitales = {}
elements = soup.find_all(class_='col-md-4 country')
for element in elements :
    country = element.find('h3', class_='country-name').text.strip()
    text = element.find('div', class_='country-info').text
    capital = element.find('span', class_='country-capital').text
    print(f"{country} - {capital}")
