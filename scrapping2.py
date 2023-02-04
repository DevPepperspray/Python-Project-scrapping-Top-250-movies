import requests
import openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "TOp Tv Series"
sheet.append(['Rank','Title','Date', 'Rating'])

website = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250/"

scrap = requests.get(website)

soup = BeautifulSoup(scrap.text, 'html.parser')

extraction = soup.find('tbody', class_="lister-list").find_all('tr')

# print(len(extraction))

for extractions in extraction:

    rankNeeded = extractions.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
    infoNeeded = extractions.find('td', class_="titleColumn").a.text
    dateNeeded = extractions.find('td', class_="titleColumn").span.text
    ratingNeeded = extractions.find('td', class_="ratingColumn imdbRating").strong.text

    print(rankNeeded)
    print(infoNeeded)
    print(dateNeeded)
    print(ratingNeeded)

    sheet.append([rankNeeded, infoNeeded, dateNeeded, ratingNeeded])
    excel.save('Top tv series.xlsX')


for extractions = 


