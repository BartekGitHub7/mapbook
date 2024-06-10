import requests
from bs4 import BeautifulSoup

def get_cordinates()->list:
    nazwa_miejscowości = input('podaj nazwę miejscowości: ')

    url:str=f'https://pl.wikipedia.org/wiki/{nazwa_miejscowości}'
    response=requests.get(url)
    # print(response.text)
    response_html=BeautifulSoup(response.text,'html.parser')
    # print(response_html)
    response_html_lat=response_html.select('.latitude')[1].text
    response_html_lng=response_html.select('.longitude')[1].text
    print (response_html_lat)
    print (response_html_lng)
    return [response_html_lat, response_html_lng]

get_cordinates()