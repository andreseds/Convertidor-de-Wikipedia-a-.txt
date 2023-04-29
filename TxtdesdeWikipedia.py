# Importar los módulos necesarios
import requests
from bs4 import BeautifulSoup
import os

# Pedir al usuario que ingrese el título del artículo de wikipedia
title = input("Ingrese el URL del artículo de wikipedia: ")

# Construir la URL del artículo usando el título y el dominio de wikipedia
url = f"https://es.wikipedia.org/wiki/{title}"

# Hacer una solicitud GET a la URL y obtener el contenido HTML
response = requests.get(url)
html = response.text

# Crear una instancia de BeautifulSoup con el contenido HTML y el analizador "lxml"
soup = BeautifulSoup(html, "lxml")

# Extraer el título, el resumen y las secciones del artículo
title = soup.find("h1", id="firstHeading").text
summary = soup.find("div", id="mw-content-text").find("p").text
sections = soup.find_all("span", class_="mw-headline")

# Crear un archivo de texto con el mismo nombre que el título y abrirlo en modo escritura
filename = f"{title}.txt"
file = open(filename, "w")

# Escribir el título, el resumen y las secciones del artículo en el archivo de texto
file.write(f"{title}\n\n")
file.write(f"{summary}\n\n")
for section in sections:
    file.write(f"{section.text}\n\n")

# Cerrar el archivo de texto
file.close()

# Mostrar un mensaje de éxito al usuario
print(f"El artículo {title} ha sido guardado en el archivo {filename}")