import csv
import requests
from bs4 import BeautifulSoup
i = 1
while i < 4 :
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    elements = soup.find_all(class_='team')

    for element in elements:
        name = element.find('td', class_='name').text.strip()
        year = element.find('td', class_='year').text.strip()
        try:
            percent = element.find('td', class_='pct text-success').text.strip()
        except:
            percent = element.find('td', class_='pct text-danger').text.strip()
        print(f'{name}-{year}-{percent}')
    i = i+1

j = 1
while j < 11 :
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={j}"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    elements = soup.find_all(class_='team')
    entete = ["Nom", "Année", "Victoire", "Défaite", "OT loose", "Pourcentage victoire", "But pour", "But contre", "+/-"]
    with open ('data.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(entete)
        for element in elements:
            try:
                diff = element.find('td', class_='diff text-success').text.strip()
                name = element.find('td', class_='name').text.strip()
                year = element.find('td', class_='year').text.strip()
                try:
                    percent = element.find('td', class_='pct text-success').text.strip()
                except:
                    percent = element.find('td', class_='pct text-danger').text.strip()
                win = element.find('td', class_='wins').text.strip()
                loose = element.find('td', class_='losses').text.strip()
                ot = element.find('td', class_='ot-losses').text.strip()
                ga = element.find('td', class_='ga').text.strip()
                gf = element.find('td', class_='gf').text.strip()
                row = [name, year, win, loose, ot, percent, gf, ga, diff]
                writer.writerow(row)
            except:
                print()
    j = j+1