from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate
import pykakasi

kakasi = pykakasi.kakasi()

product_id = []
product_name = []
product_price = []
product_img = []
base_url = "https://www.hobbystation-single.jp"

df = pd.DataFrame()

op_url = "https://www.hobbystation-single.jp/op/product/list?HbstSearchOptions[0][id]=55&HbstSearchOptions[0][search_keyword]=(BANNER)%E3%83%96%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%91%E3%83%83%E3%82%AF%20%E7%8E%8B%E6%97%8F%E3%81%AE%E8%A1%80%E7%B5%B1%E3%80%90OP-10%E3%80%91(BANNER)&HbstSearchOptions[0][Type]=2"
db_url = "https://www.hobbystation-single.jp/db/product/list?HbstSearchOptions[0][id]=80&HbstSearchOptions[0][search_keyword]=(BANNER)%E3%83%96%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%91%E3%83%83%E3%82%AF%E3%80%80%E9%99%90%E7%95%8C%E3%82%92%E8%B6%85%E3%81%88%E3%81%97%E8%80%85%5BFB04%5D(BANNER)&HbstSearchOptions[0][Type]=2"
dg_url = "https://www.hobbystation-single.jp/dg/product/list?HbstSearchOptions[0][id]=100&HbstSearchOptions[0][search_keyword]=(BANNER)%E3%80%90EX-08%E3%80%91%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E3%83%96%E3%83%BC%E3%82%B9%E3%82%BF%E3%83%BC%20CHAIN%20OF%20LIBERATION(BANNER)&HbstSearchOptions[0][Type]=2"

page_to_scrape = requests.get(dg_url)
print(f'Succesfull Request...')

kakasi.setMode("H", "a")  # Hiragana to ASCII
kakasi.setMode("K", "a")  # Katakana to ASCII
kakasi.setMode("J", "a")  # Japanese to ASCII
kakasi.setMode("r", "Hepburn")  # Use Hepburn romanization

converter = kakasi.getConverter()

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

dirty_id = soup.find_all("div", style="text-align:center;border: none; color: navy; font-size:small; background-color: lightcyan;")
dirty_name = soup.find_all("div", attrs={"class":"list_product_Name_sp"})
dirty_price = soup.find_all("div", attrs={"class" : "packageDetail"})
figure_images = soup.find_all("figure")


for i in dirty_id:
    product_id.append(i.get_text(strip=True))

for i in dirty_name:
    text = i.get_text(strip=True)
    romanized = converter.do(text)
    product_name.append(romanized)

for i in dirty_price:
    text = i.get_text(strip=True)
    price = text.split("円")[0] + "円"
    product_price.append(price)

for i in figure_images:
    img = i.find("img")['src']
    img_link = base_url + img
    product_img.append(img_link)

df['product_id'] = product_id
df['product_name'] = product_name
df['product_price'] = product_price
df['product_img'] = product_img

print(tabulate(df, headers='keys', tablefmt='psql'))

