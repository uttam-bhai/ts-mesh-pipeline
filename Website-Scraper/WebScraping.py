import pandas as pd
from lxml import etree
import requests
from IPython.display import HTML
from bs4 import BeautifulSoup

url = 'https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid'
response =requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
# print(type(response))

tables = etree.HTML(str(soup))
table = (tables.xpath('//*[@id="main-content"]/div/main/div[1]/div/table')[0].text)


columns =soup.find(id="main-content").find('table').find_all('tr')

def get_topics_titles(columns):
    selection_class = etree.HTML(str(columns))
    dom = (selection_class.xpath('//*[@id="main-content"]/div/main/div[1]/div/table')[0].text)
    test = columns.find(id="main-content").find('table').find_all('tr')
    lis1 = []
    for i in test:
        tups = i.find_all('a')
        print(tups)

get_topics_titles(soup)
#
table_df = pd.read_html(str(soup))[0]
print(table_df)

table_df.to_csv('table_df.csv')