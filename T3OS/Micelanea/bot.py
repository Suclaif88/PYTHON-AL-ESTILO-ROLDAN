from selenium import webdriver
from bs4 import BeautifulSoup

# Configuración de Selenium WebDriver
driver = webdriver.Chrome()  # Puedes usar otro navegador cambiando el driver aquí

# Navegar a la página web deseada
url = 'https://www.themoviedb.org/movie/1011985-kung-fu-panda-4?language=es      '  # Reemplaza esto con la URL de la página que quieres recopilar
driver.get(url)

# Esperar a que la página cargue completamente (puedes ajustar este tiempo según tus necesidades)
driver.implicitly_wait(10)  # Esperar hasta 10 segundos

# Obtener el HTML de la página después de que se haya cargado completamente
html = driver.page_source

# Analizar el HTML con BeautifulSoup para extraer la información deseada
soup = BeautifulSoup(html, 'html.parser')

# Ejemplo de extracción de información: encontrar todos los elementos <a> y mostrar sus textos
links = soup.find_all('a')
for link in links:
    print(link.get_text())  # Imprimir el texto de los enlaces

# Cerrar el navegador WebDriver
driver.quit()

# Generar el archivo HTML con la información recopilada
with open('informacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Archivo HTML generado exitosamente.")
