import psycopg2
import requests
from bs4 import BeautifulSoup as bs

connection = psycopg2.connect(
            dbname="parsing",
            host="localhost",
            user="postgres",
            password="usi1103",
            port=5432
        )

cursor = connection.cursor()

# globus_page = requests.get(
#     url='https://globus-online.kg/catalog/myaso_ptitsa_ryba/'
# )
# data = bs(globus_page.text, 'html.parser')


# view_showcase = data.find("div", attrs={"id": "view-showcase"})
# all_cards = view_showcase.find_all("div", class_='list-showcase__part-main')

# for card in all_cards:
#     image_link = card.find('div', class_='list-showcase__picture').a.img.get('src')
#     product_name = card.find('div', class_ = 'list-showcase__name-rating').a.text
#     price = card.find("div", class_ = 'list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text

globus_vegetables_page = requests.get(
    url='https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/'
)
data_1 = bs(globus_vegetables_page.text, 'html.parser')

view_showcase = data_1.find("div", attrs={"id": "view-showcase"})
all_cards = view_showcase.find_all("div", class_='list-showcase__part-main')

for card in all_cards:
    image_link = card.find('div', class_='list-showcase__picture').a.img.get('src')
    product_name = card.find('div', class_ = 'list-showcase__name-rating').a.text
    price = card.find("div", class_ = 'list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text


#     cursor.execute(
#         f'INSERT INTO vegetables(image, product_name, price) VALUES(\'{image_link}\', \'{product_name}\', \'{price}\');'
#     )
#     connection.commit()

# connection.close()
