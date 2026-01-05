import bs4 
import requests 

resultado = requests.get('https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1&courseCategory=Excel')
sopa=bs4.BeautifulSoup(resultado.text,'lxml')
imagenes= sopa.select('img')[0]['src']

print(imagenes)

imagen_curso= requests.get(imagenes)


f=open('mi_imagen.jpg','wb')
f.write(imagen_curso.content)
f.close()