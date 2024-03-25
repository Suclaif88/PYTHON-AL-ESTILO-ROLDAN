import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

def extraer_h3_desde_pagina(url_pagina):
    response = requests.get(url_pagina)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        h3_tags = soup.find_all('h3')

        for h3_tag in h3_tags:
            print(h3_tag.text)
    else:
        print("Error al acceder a la página:", response.status_code)

url_pagina = 'https://www.boxofficemojo.com/calendar/2022-01-01/'

extraer_h3_desde_pagina(url_pagina)