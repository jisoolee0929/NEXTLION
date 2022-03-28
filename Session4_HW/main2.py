import requests
from bs4 import BeautifulSoup
import csv
from Webtoon import extract_Webtoon

file = open('Sat_webtoon.csv', mode = 'w', newline = "")
writer = csv.writer(file)
writer.writerow(["title", "writer","rating"])


Webtoon_URL = f"https://comic.naver.com/webtoon/weekdayList?week=sat"
Webtoon_html = requests.get(Webtoon_URL)
Webtoon_soup = BeautifulSoup(Webtoon_html.text,"html.parser")
Webtoon_listbox = Webtoon_soup.find('ul',{'class':"img_list"})
Webtoon_list = Webtoon_listbox.find_all('dl')

result = extract_Webtoon(Webtoon_list)

for webtoon in result:
    row = []
    row.append(webtoon['title'])
    row.append(webtoon['writer'])
    row.append(webtoon['rating'])
    writer.writerow(row)
