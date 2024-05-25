import requests
from bs4 import BeautifulSoup

# Función para obtener la información de películas desde una URL
def obtener_informacion_peliculas(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Aquí debes identificar los elementos HTML que contienen la información de las películas
        peliculas = soup.find_all('div', class_='pelicula')
        return peliculas
    else:
        print("Error al obtener la página:", response.status_code)
        return []

# Función para generar el archivo HTML
def generar_pagina_html(peliculas_por_categoria):
    with open('pagina_cine.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="es">\n')
        f.write('<head>\n')
        f.write('<meta charset="UTF-8">\n')
        f.write('<title>Cartelera de Cine</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        
        for categoria, peliculas in peliculas_por_categoria.items():
            f.write(f'<h2>{categoria}</h2>\n')
            f.write('<ul>\n')
            for pelicula in peliculas:
                f.write(f'<li>{pelicula}</li>\n')
            f.write('</ul>\n')
        
        f.write('</body>\n')
        f.write('</html>\n')

# URL de donde obtendremos la información (reemplaza esto con la URL real)
url_cine = 'https://www.themoviedb.org/movie?language=es'
# Obtener la información de películas por categorías
peliculas_por_categoria = {
    'Acción': obtener_informacion_peliculas(url_cine + '/accion'),
    'Comedia': obtener_informacion_peliculas(url_cine + '/comedia'),
    'Drama': obtener_informacion_peliculas(url_cine + '/drama'),
    # Agrega más categorías según sea necesario
}

# Generar la página HTML con la información recopilada
generar_pagina_html(peliculas_por_categoria)
print("Página HTML generada exitosamente.")
