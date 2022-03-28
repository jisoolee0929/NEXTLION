import requests
from bs4 import BeautifulSoup
import re

def extract_Webtoon(webtoon_list):
    # 제목 구하기
    result = []
    title_list = ""
    for webtoon in webtoon_list:
        title_html = webtoon.find("dt")
        title_list += str(title_html)
    title = re.findall(r'title=".+"',title_list)
    for i in range(len(title)):
        title[i] = title[i].lstrip("title=").strip('"')
        #print(title[i])
    writer_list=[]
    #작가 이름
    for webtoon in webtoon_list:
        writer_html = webtoon.find("dd").find('a')
        writer_list += writer_html
    #print(writer_list)
    rating_list = []
    for webtoon in webtoon_list:
        rating_html = webtoon.find('strong')
        rating_list += rating_html
    #print(rating_list)

    for i in range(len(title)):
        webtoon_info = {
            "title":title[i],
            "writer":writer_list[i],
            "rating":rating_list[i],
        }
        result.append(webtoon_info)
    #print(result)

    return result
    


