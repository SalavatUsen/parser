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

itc_page = requests.get(
    url='https://www.itc.kg/'
)
data = bs(itc_page.text, 'html.parser')

section = data.find('section', attrs={"id": "service"})
all_col_md_4 = section.find_all('div', class_="col-md-4")


for col in all_col_md_4:
    name = col.h2.get_text()

    definition = col.p.text.strip().split('\n')

    if definition[-1] == 'Подробнее':
        definition.pop(-1)

    definition = ' '.join([i.strip() for i in definition])
    # print(definition)

    cursor.execute(f'INSERT INTO services(name, definition) VALUES(\'{name}\', \'{definition}\')')
    connection.commit()
