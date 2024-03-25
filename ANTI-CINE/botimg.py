import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

def descargar_imagenes_desde_pagina(url_pagina, directorio_destino):
    response = requests.get(url_pagina)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        imagenes = soup.find_all('img')

        contador = 1  # Inicializar el contador

        for imagen in imagenes:
            url_imagen = imagen['src']
            
            if urlparse(url_imagen).scheme:
                # Obtener la extensión de la imagen
                extension = os.path.splitext(url_imagen)[1]
                
                # Construir el nombre de archivo usando el contador y la extensión
                nombre_imagen = f"{contador}{extension}"
                
                response_imagen = requests.get(url_imagen)
                
                if response_imagen.status_code == 200:
                    with open(os.path.join(directorio_destino, nombre_imagen), 'wb') as archivo:
                        archivo.write(response_imagen.content)
                    print(f"Imagen '{nombre_imagen}' descargada exitosamente.")
                    
                    contador += 1  # Incrementar el contador
                else:
                    print(f"Error al descargar la imagen '{nombre_imagen}': {response_imagen.status_code}")
            else:
                print(f"La URL '{url_imagen}' no es válida.")
    else:
        print("Error al acceder a la página:", response.status_code)

url_pagina = 'https://www.boxofficemojo.com/calendar/2022-01-01/'
directorio_destino = 'imagenes_descargadas'
os.makedirs(directorio_destino, exist_ok=True)

descargar_imagenes_desde_pagina(url_pagina, directorio_destino)
