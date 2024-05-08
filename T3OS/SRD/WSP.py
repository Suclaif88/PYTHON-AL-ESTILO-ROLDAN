from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Abrir WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Esperar a que se cargue la ventana de WhatsApp Web
wait = WebDriverWait(driver, 60)

# Buscar el contacto
target = '"Contact Name"'
contact = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{target}"]')))
contact.click()

# Esperar a que se cargue la ventana de chat
input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_1Plpp"]//div[@class="_3uMse"]')))

# Escribir el mensaje
input_box.send_keys("SIGUE A ROLDI")

# Enviar el mensaje
input_box.send_keys(Keys.RETURN)

# Cerrar el navegador
driver.quit()