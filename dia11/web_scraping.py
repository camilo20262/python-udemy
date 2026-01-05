import bs4 
import requests 

resultado = requests.get('https://escueladirecta.com/')
sopa=bs4.BeautifulSoup(resultado.text,'lxml')
#print(sopa)

print(sopa.select('title'))

