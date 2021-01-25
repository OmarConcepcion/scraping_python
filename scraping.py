from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://panadata.net/es/panadata'
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")

important_info = soup.find_all('p', class_='text-4')

lista_info = list()

for i in important_info:
    # Se elimina informacion no necesaria
    if (i.text != "\nFUNCIONALIDADES DESTACADAS\n"):
        texto = i.text
        # elimino los saltos de linea
        texto = texto.strip('\n')
        texto = texto.strip('\n\n')
        texto.replace("\n", "")
        texto.replace("\n\n", "")
        print ("\n"+texto.replace("\n", ""))


